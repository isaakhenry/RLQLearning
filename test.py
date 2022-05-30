import matplotlib.pyplot as plt
import gym
import numpy as np
import math
import tensorflow as tf
tf.disable_v2_behavior()
import reinforcement_learning as rl
tf.__version__
gym.__version__

env = gym.make("ALE/WizardOfWor-v5", render_mode = 'human')
env.reset()
for _ in range(1000):
    action = env.action_space.sample() # take a random action
    observation, reward, done, info = env.step(action)
    
    