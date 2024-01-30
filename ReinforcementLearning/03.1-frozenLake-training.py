#Referência1: https://github.com/simoninithomas/Deep_reinforcement_learning_Course/blob/master/Q%20learning/FrozenLake/Q%20Learning%20with%20FrozenLake.ipynb
#Referência2: https://towardsdatascience.com/q-learning-for-beginners-2837b777741

##### DESCRIÇÃO #####
#O código a seguir treina um agente para o jogo Frozen-Lake usando Reinforcement Learning.
#O código apenas treina, sem apresentar o jogo de maneira gráfica.
#O código atual aprende e exporta a tabela Q como um numpy array, a qual será carregada no arquivo de teste.
#Considerando que a tabela Q é aprendida, no código de teste o jogo é renderizado (graficamente) para observarmos os resultado do agente.

import gym
import numpy as np
import random
from config_games import *

my_map = frozen_lake_maps[CURR_MAP].copy() #Get the created map from config_games.py

# 1. Load Environment and Q-table structure
env = gym.make('FrozenLake-v1', desc=my_map, is_slippery=False) # try for different environments

# 1.1 The env.observation.n, env.action_space.n gives number of states and action in env loaded
action_size = env.action_space.n     #Number of possible actions, in this case Up, Down, Left, Right = 4 actions
state_size = env.observation_space.n #Number of possible states, in this case a board 4x4 = 16 states
qtable = np.zeros([state_size, action_size])

print(f"N size = {action_size}, N states = {state_size}")

# 2.1 Parameters of Q-learning
total_episodes = 1000         # Total episodes
learning_rate = 0.8           # Learning rate
max_steps = 30                # Max steps per episode
gamma = 0.95                  # Discounting rate

# 2.2 Exploration parameters
epsilon = 1.0                 # Exploration rate
max_epsilon = 1.0             # Exploration probability at start
min_epsilon = 0.01            # Minimum exploration probability 
decay_rate = 0.005            # Exponential decay rate for exploration prob

# 3. Q-learning Algorithm
# List of rewards
rewards = []

#Actions: ◀️ LEFT = 0, 🔽 DOWN = 1, ▶️ RIGHT = 2, 🔼 UP = 3
actions_to_solve = [2,2,1,1,1,2] # Only for test purposes
SOLVE_AUTOMATICALLY = False      # Uses an automatic route set manually to solve the game if True
DEBUG = True                     # Print the metrics if True

# 2 For life or until learning is stopped
for episode in range(total_episodes):
    # Reset the environment
    state, _ = env.reset()
    step = 0
    done = False
    total_rewards = 0
    
    for step in range(max_steps):
        # 3. Choose an action a in the current world state (s)
        ## First we randomize a number
        exp_exp_tradeoff = random.uniform(0, 1)
        
        ## If this number > greater than epsilon --> exploitation (taking the biggest Q value for this state)
        if exp_exp_tradeoff > epsilon:
            action = np.argmax(qtable[state,:])

        # Else doing a random choice --> exploration
        else:
            action = env.action_space.sample()
        
        # The following code uses a manual route to solve the game (Only for test purposes)
        if SOLVE_AUTOMATICALLY:
            action = actions_to_solve[step%len(actions_to_solve)]

        # Take the action (a) and observe the outcome state(s') and reward (r)
        new_state, reward, done, info, _ = env.step(action)

        # Update Q(s,a):= Q(s,a) + lr [R(s,a) + gamma * max Q(s',a') - Q(s,a)]
        # qtable[new_state,:] : all the actions we can take from new state
        qtable[state, action] = qtable[state, action] + learning_rate * (reward + gamma * np.max(qtable[new_state, :]) - qtable[state, action])
        
        total_rewards += reward
        
        # Our new state is state
        state = new_state
        
        # If done (if we're dead) : finish episode
        if done == True: 
            break
        
    # Reduce epsilon (because we need less and less exploration)
    epsilon = min_epsilon + (max_epsilon - min_epsilon)*np.exp(-decay_rate*episode) 
    rewards.append(total_rewards)

    if DEBUG:
        print(f"Episode = {episode} ----> Score = {sum(rewards)/total_episodes}")

print("Final Score: " + str(sum(rewards)/total_episodes))
print("---------- Q-table Learned ----------")
print(qtable)

#Save the Q-Table learned
np.save("03-qtable_frozen_lake.npy", qtable)