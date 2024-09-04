import numpy as np
import parameters as pr
import propogation

def binary_cross_entropy_loss(A2, true_label):
    epsilon = 1e-10
    A2 = np.clip(A2, epsilon, 1 - epsilon)
    m = true_label.shape[0]
    loss = -(1/m) * np.sum(true_label * np.log(A2) + (1-true_label) * np.log(1-A2))
    return loss


def train(input_data, true_label, hidden_layer_size, num_iteration, learning_rate):
    parameters = pr.initialize_parameters(input_data.shape[1], hidden_layer_size, 1)

    for i in range(num_iteration):
        A2, cache = propogation.forward_propagation(input_data, parameters)

        loss = binary_cross_entropy_loss(A2, true_label)

        gradient = propogation.backward_propagation(parameters, cache, input_data, true_label)

        parameters = pr.update_parameters(parameters, gradient, learning_rate)

        if i % 1000 == 0:
            print(f"iteration {i}: loss {loss}")

    return parameters

def predict(input_data, parameters):
    A2, _ = propogation.forward_propagation(input_data, parameters)
    print(f"A2 shape after forward propagation: {A2.shape}")
    predictions = (A2 > 0.5).astype(int)
    return predictions
