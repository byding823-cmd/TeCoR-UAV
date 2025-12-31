import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np


class SharedActorCritic(nn.Module):
    def __init__(self, obs_dim, n_agents, action_dim, hidden_dim=128):
        super().__init__()
        self.n_agents = n_agents
        self.action_dim = action_dim

        self.actor_fc1 = nn.Linear(obs_dim, hidden_dim)
        self.actor_fc2 = nn.Linear(hidden_dim, hidden_dim)
        self.critic_fc1 = nn.Linear(obs_dim, hidden_dim)
        self.critic_fc2 = nn.Linear(hidden_dim, hidden_dim)

        self.actor_heads = nn.ModuleList(
            [nn.Linear(hidden_dim, action_dim) for _ in range(n_agents)]
        )

        self.critic_head = nn.Linear(hidden_dim, 1)

    def forward(self, x):
        a_x = torch.relu(self.actor_fc1(x))
        a_x = torch.relu(self.actor_fc2(a_x))
        logits = torch.stack([head(a_x) for head in self.actor_heads], dim=1)

        c_x = torch.relu(self.critic_fc1(x))
        c_x = torch.relu(self.critic_fc2(c_x))
        value = self.critic_head(c_x).squeeze(-1)
        return logits, value

    def actor_parameters(self):
        return list(self.actor_fc1.parameters()) + list(self.actor_fc2.parameters()) + list(self.actor_heads.parameters())

    def critic_parameters(self):
        return list(self.critic_fc1.parameters()) + list(self.critic_fc2.parameters()) + list(self.critic_head.parameters())


class MAPPOAgent:
    def __init__(self, obs_dim, n_agents, action_dim, lr_actor=1e-4, lr_critic=1e-3, gamma=0.99, clip_epsilon=0.2,
                 entropy_coef=0.02, gae_lambda=0.92, value_coef=0.5):
        self.n_agents = n_agents
        self.action_dim = action_dim
        self.gamma = gamma
        self.clip_epsilon = clip_epsilon
        self.entropy_coef = entropy_coef
        self.gae_lambda = gae_lambda
        self.value_coef = value_coef
        self.model = SharedActorCritic(obs_dim, n_agents, action_dim)
        self.actor_optimizer = optim.Adam(self.model.actor_parameters(), lr=lr_actor)
        self.critic_optimizer = optim.Adam(self.model.critic_parameters(), lr=lr_critic)

    def act(self, state):
        state_tensor = torch.FloatTensor(state).unsqueeze(0)  # [1, obs_dim]
        logits, value = self.model(state_tensor)  # logits: [1, n_agents, action_dim], value: [1]

        actions = []
        log_probs = []

        for agent_idx in range(self.n_agents):
            dist = torch.distributions.Categorical(logits=logits[0, agent_idx])
            action = dist.sample()
            actions.append(action.item())
            log_probs.append(dist.log_prob(action))

        return actions, torch.stack(log_probs), value

    def update(self, trajectories):
        states = torch.FloatTensor(np.array([t['state'] for t in trajectories]))  # [batch, obs_dim]
        next_states = torch.FloatTensor(np.array([t['next_state'] for t in trajectories]))
        actions = torch.LongTensor([t['actions'] for t in trajectories])  # [batch, n_agents]
        old_log_probs = torch.stack([t['log_probs'] for t in trajectories])  # [batch, n_agents]
        rewards = torch.FloatTensor(np.array([t['reward'] for t in trajectories]))  # 关键修复点
        dones = np.array([t['done'] for t in trajectories])
        old_values = torch.stack([t['value'] for t in trajectories]).squeeze(-1)  # [batch]

        with torch.no_grad():
            _, next_values = self.model(next_states)  # [batch]
            next_values = next_values * (1 - dones)

        advantages = torch.zeros_like(rewards)
        gae = 0
        for t in reversed(range(len(rewards) - 1)):
            delta = rewards[t] + self.gamma * next_values[t] - old_values[t]
            gae = delta + self.gamma * self.gae_lambda * (1 - dones[t]) * gae
            advantages[t] = gae
        returns = advantages + old_values  # [batch]

        logits, values_pred = self.model(states)  # logits: [batch, n_agents, action_dim]

        entropy = []
        log_probs_new = []
        for i in range(self.n_agents):
            dist = torch.distributions.Categorical(logits=logits[:, i, :])
            log_probs_new.append(dist.log_prob(actions[:, i]))
            entropy.append(dist.entropy())
        log_probs_new = torch.stack(log_probs_new, dim=1)  # [batch, n_agents]
        entropy = torch.stack(entropy, dim=1).mean()  # 标量

        ratio = torch.exp(log_probs_new - old_log_probs.detach())  # [batch, n_agents]
        advantages = advantages.unsqueeze(1).expand(-1, self.n_agents)  # 广播到每个智能体
        surr1 = ratio * advantages
        surr2 = torch.clamp(ratio, 1 - self.clip_epsilon, 1 + self.clip_epsilon) * advantages
        actor_loss = -torch.min(surr1, surr2).mean() - self.entropy_coef * entropy

        values_pred_clipped = old_values + torch.clamp(
            values_pred - old_values,
            -self.clip_epsilon,
            self.clip_epsilon
        )

        critic_loss_unclipped = nn.MSELoss()(values_pred, returns)
        critic_loss_clipped = nn.MSELoss()(values_pred_clipped, returns)

        critic_loss = torch.max(critic_loss_unclipped, critic_loss_clipped)

        self.actor_optimizer.zero_grad()
        actor_loss.backward(retain_graph=True)
        torch.nn.utils.clip_grad_norm_(
            self.model.actor_parameters(),
            max_norm=0.5,
            norm_type=2
        )
        self.actor_optimizer.step()

        self.critic_optimizer.zero_grad()
        critic_loss.backward()
        torch.nn.utils.clip_grad_norm_(
            self.model.critic_parameters(),
            max_norm=0.5,
            norm_type=2
        )
        self.critic_optimizer.step()

        if hasattr(self, 'actor_scheduler'):
            self.actor_scheduler.step()
        if hasattr(self, 'critic_scheduler'):
            self.critic_scheduler.step()

        return {
            'actor_loss': actor_loss.item(),
            'critic_loss': critic_loss.item(),
            'critic_loss_unclipped': critic_loss_unclipped.item(),  # 原始损失
            'critic_loss_clipped': critic_loss_clipped.item(),      # 裁剪后损失
            'entropy': entropy.item(),
            'avg_advantage': advantages.mean().item(),
            'value_pred_mean': values_pred.mean().item(),
            'returns_mean': returns.mean().item()
        }
