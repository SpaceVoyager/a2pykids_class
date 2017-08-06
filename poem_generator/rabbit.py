import random
import numpy as np

states = ['sleep', 'eat']
state = np.random.choice(states, p=[0.5, 0.5])

rabbit_states = [state]

for hour in range(24*7):
    if state == 'sleep':
        state = np.random.choice(states, p=[0.7, 0.3])
    elif state == 'eat':
        state = np.random.choice(states, p=[0.9, 0.1])
    rabbit_states.append(state)

print rabbit_states

for i in range(len(rabbit_states)-1):
    curr_state = rabbit_states[i]
    next_state = rabbit_states[i+1]

