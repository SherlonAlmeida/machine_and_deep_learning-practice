# 1. It renders instances for 200 timesteps, performing random actions.
import gym
env = gym.make('Mountaincar-v0', render_mode="human")

timesteps = 200
env.reset() 

for _ in range(timesteps):
    env.render()
    env.step(env.action_space.sample())
    print(_)

# 2. To check all env available, uninstalled ones are also shown.
from gym import envs 
for idx, curr_env in enumerate(envs.registry.items()):
    print(idx, curr_env, end="\n\n")