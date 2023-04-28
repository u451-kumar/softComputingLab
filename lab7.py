import numpy as np

class SingleLayerFeedForward:
    def __init__(self, input_size, output_size, activation_function):
        self.input_size = input_size
        self.output_size = output_size
        self.activation_function = activation_function
        
        # Initialize weights randomly
        self.weights = np.random.randn(output_size, input_size)
        
    def forward(self, inputs):
        # Compute dot product of inputs and weights
        dot_product = np.dot(self.weights, inputs)
        
        # Apply activation function
        output = self.activation_function(dot_product)
        
        return output

class HebbianLearning:
    def __init__(self, input_size, output_size):
        self.input_size = input_size
        self.output_size = output_size
        
        # Initialize weight matrix to zeros
        self.weights = np.zeros((output_size, input_size))
        
    def train(self, inputs):
        # Apply Hebb's Rule to update weights
        self.weights += np.outer(inputs, inputs)
        
        # Ensure weights are symmetric
        self.weights = np.maximum(self.weights, self.weights.T)

# Define input vector and activation function
input_vector = np.array([0.5, 0.2, 0.1])
sigmoid = lambda x: 1 / (1 + np.exp(-x))

# Create single layer feed forward neural network
network = SingleLayerFeedForward(3, 2, sigmoid)

# Compute output of network
output = network.forward(input_vector)
print("Output of network:", output)

# Apply Hebb's Rule to update weights
hebb = HebbianLearning(3, 2)
hebb.train(input_vector)
print("New weights:", hebb.weights)
