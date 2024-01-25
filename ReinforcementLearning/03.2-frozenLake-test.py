import gym
import numpy as np
import random
from config_games import *

my_map = frozen_lake_maps["4x4"] #Get the created map from config_games.py

# 1. Load Environment and Q-table structure
env = gym.make('FrozenLake-v1', desc=my_map, is_slippery=False, render_mode="human") # try for different environments

# 1.1 The env.observation.n, env.action_space.n gives number of states and action in env loaded
action_size = env.action_space.n     #Number of possible actions, in this case Up, Down, Left, Right = 4 actions
state_size = env.observation_space.n #Number of possible states, in this case a board 4x4 = 16 states

#Load the pre-treined Q-Table
qtable = np.load("03-qtable_frozen_lake.npy")

print(f"N size = {action_size}, N states = {state_size}")

# 2.1 Parameters of Q-learning
total_episodes = 5            # Total episodes
max_steps = 15                # Max steps per episode

# 3. Q-learning Algorithm
# List of rewards
rewards = []

#Actions: ◀️ LEFT = 0, 🔽 DOWN = 1, ▶️ RIGHT = 2, 🔼 UP = 3
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
        action = np.argmax(qtable[state,:])
        
        # Take the action (a) and observe the outcome state(s') and reward (r)
        new_state, reward, done, info, _ = env.step(action)
        total_rewards += reward
        
        # Our new state is state
        state = new_state

        if DEBUG:
            print(f"Episode = {episode} ----> step = {step} ----> Reward = {total_rewards}")
        
        # If done (if we're dead) : finish episode
        if done == True: 
            break
        
    rewards.append(total_rewards)

print ("Score over time: " +  str(sum(rewards)/total_episodes))
print(qtable)