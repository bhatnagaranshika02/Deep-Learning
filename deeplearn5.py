import numpy as np
input_data = np.array([0,3])
weights_0 = {'node_0':[2,1],
             'node_1':[1,2],
             'output':[1,1]
             }
target_actual = 3
model_output_0  = predict_with_network(input_data , weights_0)
error_0 = model_output_0 - target_actual


weights_1 = {'node_0': [2, 1],
             'node_1': [1, 2],
             'output': [1, 0]
            }

# Make prediction using new weights: model_output_1
model_output_1 = predict_with_network(input_data, weights_1)

# Calculate error: error_1
error_1 = model_output_1 - target_actual
print(error_0)
print(error_1)

