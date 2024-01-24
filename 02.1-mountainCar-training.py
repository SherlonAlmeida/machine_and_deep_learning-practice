##### DESCRIÇÃO #####
#O código a seguir treina um agente para o jogo Mountain Car usando Reinforcement Learning.
#O código apenas treina, sem apresentar o jogo de maneira gráfica.
#O código atual aprende e exporta a tabela Q como um numpy array, a qual será carregada no arquivo de teste.
#Considerando que a tabela Q é aprendida, no código de teste o jogo é renderizado (graficamente) para observarmos os resultado do agente.

import gym
import numpy as np
import random

# 1. Load Environment and Q-table structure
env = gym.make('MountainCarContinuous-v0') # try for different environments

env = gym.make('MountainCarContinuous-v0', render_mode="human") # try for different environments
observation = env.reset()
timesteps = 100

for t in range(timesteps):
    env.render()
    action = env.action_space.sample() #Random
    observation, reward, done, info, _ = env.step(action)
    print (t, action, observation, reward, done, info)
    
    if done:
        print("Finished after {} timesteps".format(t+1))
        break

#Ainda preciso implementar esta parte.