import numpy as np
import parameters as pr
import propogation
import train_and_predict     


np.random.seed(0)

input_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
input_data = np.array(input_data, dtype=float)
true_label = np.array([[0], [1], [1], [0]])
true_label = np.array(true_label, dtype=float)
parameters = pr.initialize_parameters(2, 3, 1)
A2, cache = propogation.forward_propagation(input_data, parameters)
print("final activation: ", A2)
parameters = train_and_predict.train(input_data, true_label, hidden_layer_size=4, num_iteration=10000, learning_rate=0.1)
preditions = train_and_predict.predict(input_data, parameters)
print("final prediction: ")
print(preditions)
