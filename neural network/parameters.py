import numpy as np


def initialize_parameters(input_size, hidden_size, output_size):
    np.random.seed(0)

    weight_1= np.random.randn(hidden_size, input_size) * 0.01
    bias_1 = np.zeros((hidden_size, 1))
    weight_2 = np.random.randn(output_size, hidden_size) * 0.01
    bias_2 = np.zeros((output_size, 1))
    parameters = {"weight_1":weight_1 , "bias_1":bias_1, "weight_2":weight_2, "bias_2":bias_2}
    return parameters

def update_parameters(parameters, gradient, learning_rate):
    derive_weight_1 = gradient["derive_weight_1"]
    derive_bias_1 = gradient["derive_bias_1"]
    derive_weight_2 = gradient["derive_weight_2"]
    derive_bias_2 = gradient["derive_bias_2"]

    weight_1 = parameters["weight_1"]
    bias_1 = parameters["bias_1"]
    weight_2 = parameters["weight_2"]
    bias_2 = parameters["bias_2"]

    weight_1 = weight_1 - learning_rate * derive_weight_1
    bias_1 = bias_1 - learning_rate * derive_bias_1
    weight_2 = weight_2 - learning_rate * derive_weight_2
    bias_2 = bias_2 - learning_rate * derive_bias_2

    parameters = {
        "weight_1": weight_1,
        "bias_1": bias_1,
        "weight_2": weight_2,
        "bias_2": bias_2
    }

    return parameters