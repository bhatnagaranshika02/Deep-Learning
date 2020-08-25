import numpy as np
weights = np.array([1, 2])
input_data = np.array([3, 4])
target = 6
learning_rate = 0.01

preds = (weights*input_data).sum()
error = preds - target
slope = input_data * error * 2
print(slope)
