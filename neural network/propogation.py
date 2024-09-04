import numpy as np


def sigmoid(input_data):
    return 1/(1 + np.exp(-input_data))

def forward_propagation(input_data, parameters):
    weight_1 = parameters["weight_1"]
    bias_1 = parameters["bias_1"]
    weight_2 = parameters["weight_2"]
    bias_2 = parameters["bias_2"]

    if input_data.shape[0] != weight_1.shape[1]:
        input_data = input_data.T
    
    Z1 = np.dot(weight_1, input_data) + bias_1
    A1 = sigmoid(Z1)

    Z2 = np.dot(weight_2, A1) + bias_2
    A2 = sigmoid(Z2)
    
    cache = {"Z1":Z1, "A1":A1, "Z2":Z2, "A2":A2}

    return A2, cache

def backward_propagation(parameters, cache, input_data, true_label):
    m = true_label.shape[0]

    A1 = cache["A1"]
    A2 = cache["A2"]

    epsilon = 1e-10
    A2 = np.clip(A2, epsilon, 1 - epsilon)

    derive_A2 = - (true_label/A2) + ((1 - true_label) / (1 - A2))
    derive_Z2 = derive_A2 * (A2 * (1 - A2))

    derive_weight_2 = (1 / m) * np.dot(derive_Z2, A1)
    derive_bias_2 = (1 / m) * np.sum(derive_Z2, axis=1, keepdims=True)

    derive_A1 = np.dot(parameters["weight_2"], derive_Z2)
    derive_Z1 = derive_A1 * (A1 * (1 - A1))

    derive_weight_1 = (1 / m) * np.dot(derive_Z1, input_data)
    derive_bias_1 = (1 / m) * np.sum(derive_Z1, axis=1, keepdims=True)
    gradients = {
        "derive_weight_1": derive_weight_1, 
        "derive_bias_1": derive_bias_1, 
        "derive_weight_2": derive_weight_2, 
        "derive_bias_2": derive_bias_2
        }
    return gradients