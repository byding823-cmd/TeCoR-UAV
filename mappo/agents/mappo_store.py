import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

class SharedActorCritic(nn.Module):
    def __init__(self, obs_dim, n_agents, action_dim, hidden_dim=128):
        super().__init__()
        self.n_agents = n_agents
        self.action_dim = action_dim

        self.fc1 = nn.Linear(obs_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, hidden_dim)

        self.actor_heads = nn.ModuleList(
            [nn.Linear(hidden_dim, action_dim) for _ in range(n_agents)]
        )

        self.critic_head = nn.Linear(hidden_dim, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        logits = torch.stack([head(x) for head in self.actor_heads], dim=1)
        value = self.critic_head(x)
        return logits, value.squeeze(-1)

class MAPPOAgent:
    def __init__(self, obs_dim, n_agents, action_dim, lr=3e-4, gamma=0.99, clip_epsilon=0.2):
        self.n_agents = n_agents
        self.action_dim = action_dim
        self.gamma = gamma
        self.clip_epsilon = clip_epsilon

        self.model = SharedActorCritic(obs_dim, n_agents, action_dim)
        self.optimizer = optim.Adam(self.model.parameters(), lr=lr)

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
        states = torch.FloatTensor(np.array([t['state'] for t in trajectories]))
        next_states = torch.FloatTensor(np.array([t['next_state'] for t in trajectories]))
        actions = torch.LongTensor([t['actions'] for t in trajectories])  # [batch, n_agents]
        old_log_probs = torch.stack([t['log_probs'] for t in trajectories])  # [batch, n_agents]
        rewards = [t['reward'] for t in trajectories]
        dones = [t['done'] for t in trajectories]
        values = torch.stack([t['value'] for t in trajectories]).squeeze(-1)  # [batch]

        with torch.no_grad():
            _, next_values = self.model(next_states)  # [batch]
            next_values = next_values * (1 - torch.tensor(dones, dtype=torch.float32))

        returns = []
        advantages = []
        gae = 0
        for step in reversed(range(len(rewards))):
            delta = rewards[step] + self.gamma * next_values[step] - values[step]
            gae = delta + self.gamma * 0.95 * gae
            returns.insert(0, gae + values[step])
        returns = torch.tensor(returns)
        advantages = returns - values

        logits, values_pred = self.model(states)  # logits: [batch, n_agents, action_dim]

        log_probs_new = []
        for i in range(self.n_agents):
            dist = torch.distributions.Categorical(logits=logits[:, i, :])
            log_prob = dist.log_prob(actions[:, i])
            log_probs_new.append(log_prob)
        log_probs_new = torch.stack(log_probs_new, dim=1)  # [batch, n_agents]

        ratio = torch.exp(log_probs_new - old_log_probs)  # [batch, n_agents]
        surr1 = ratio * advantages.unsqueeze(1)
        surr2 = torch.clamp(ratio, 1 - self.clip_epsilon, 1 + self.clip_epsilon) * advantages.unsqueeze(1)

        actor_loss = -torch.min(surr1, surr2).mean()

        critic_loss = nn.MSELoss()(values_pred, returns)

        loss = actor_loss + 0.5 * critic_loss

        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        return actor_loss.item(), critic_loss.item()
