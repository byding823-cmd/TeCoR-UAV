import json

import numpy as np
import torch
import torch.optim as optim

from envs.drone_env_new import DroneTaskEnv  # 你的环境
from agents.mappo_new import MAPPOAgent


def flatten_state(state_dict):
    return np.concatenate([
        state_dict['available'],
        state_dict['task_needed'],
        state_dict['uav_free'],
        state_dict['task_coordinates'].flatten()
    ])


def train(config_env):
    env = DroneTaskEnv(config_env)
    obs_dim = len(flatten_state(env.reset()))
    n_agents = env.num_tasks
    action_dim = env.num_uavs
    agent = MAPPOAgent(obs_dim, n_agents, action_dim)
    actor_scheduler = optim.lr_scheduler.StepLR(
        agent.actor_optimizer,
        step_size=500,
        gamma=0.8
    )
    critic_scheduler = optim.lr_scheduler.StepLR(
        agent.critic_optimizer,
        step_size=500,
        gamma=0.8
    )

    max_episodes = 1000
    max_steps = 128

    best_reward = -float('inf')
    best_actions = []

    for episode in range(max_episodes):
        if episode < max_episodes / 4:
            agent.entropy_coef = 0.1
        elif episode < max_episodes * 3 / 4:
            decay_factor = (episode - max_episodes / 4) / 1000
            agent.entropy_coef = max(0.01, 0.1 * (1 - decay_factor))
        else:
            agent.entropy_coef = 0.01
            actor_scheduler.step()
            critic_scheduler.step()

        state_dict = env.reset()
        state = flatten_state(state_dict)

        episode_rewards = 0
        trajectories = []
        episode_actions = []

        for step in range(max_steps):
            actions, log_probs, value = agent.act(state)
            episode_actions.append(actions.copy())
            next_state_dict, rewards, done, _ = env.step(actions)
            next_state = flatten_state(next_state_dict)
            reward = rewards
            transition = {
                'state': state,
                'actions': actions,
                'log_probs': log_probs,
                'reward': reward,
                'next_state': next_state,
                'done': done,
                'value': value
            }
            trajectories.append(transition)
            state = next_state
            episode_rewards += reward

            if done:
                break

        if episode_rewards > best_reward:
            best_reward = episode_rewards
            best_actions = episode_actions
            torch.save(agent.model.state_dict(), 'best_model.pth')
            with open('best_actions.json', 'w') as f:
                json.dump(best_actions, f)

            print(f"Episode {episode}: New best reward {best_reward:.2f}! Model and actions saved.")
            continue

        # 训练更新
        metrics = agent.update(trajectories)

        if episode % 10 == 0:
            print(
                f"Episode {episode}, "
                f"Reward: {episode_rewards:.2f}, "
                f"Actor loss: {metrics['actor_loss']:.4f}, "
                f"Critic loss: {metrics['critic_loss_unclipped']:.4f}, "
                f"Entropy coef: {agent.entropy_coef:.4f}")
    with open('best_actions_final.json', 'w') as f:
        json.dump(best_actions, f)
    torch.save(agent.model.state_dict(), 'mappo_agent_final.pth')
