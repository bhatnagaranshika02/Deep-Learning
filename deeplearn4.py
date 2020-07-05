import numpy as np
def predict_with_network(input_data):
    node_0_0_input = (input_data * weights['node_0_0']).sum()
    node_0_0_output = relu(node_0_0_input)
    node_0_1_input = (input_data * weights['node_0_1']).sum()
    node_0_1_output =relu(node_0_1)
    hidden_0_output =  np.array(node_0_0_output , node_0_1_output)

    node_1_0_input = (input_data * weights['node_1_0']).sum()
    node_1_0_output = relu(node_0_0_input)
    node_1_1_input = (input_data * weights['node_0_1']).sum()
    node_1_1_output =relu(node_0_1)
    hidden_1_output =  np.array(node_1_0_output , node_1_1_output)

    model_output =(hidden_1_output * weights['output'])

    return model_output


output = predict_with_network(input_data)
print(output)

    
    
