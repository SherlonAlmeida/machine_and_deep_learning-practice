#Este código apenas renderiza o jogo e realiza ações aleatórias.

import gym
import numpy as np

def get_action(t):
    action = env.action_space.sample() #Random
    return action

env = gym.make('FrozenLake-v1', render_mode="human") # try for different environments
observation = env.reset()
timesteps = 100

for t in range(timesteps):
    env.render()
    action = get_action(t)
    observation, reward, done, info, _ = env.step(action)
    print (t, action, observation, reward, done, info)
    
    if done:
        print("Finished after {} timesteps".format(t+1))
        break