import numpy as np

class MultiLayerNeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # Initialize weights randomly
        self.weights_input_hidden = np.random.randn(hidden_size, input_size)
        self.weights_hidden_output = np.random.randn(output_size, hidden_size)
        
    def forward(self, inputs):
        # Compute dot product of input and weights from input to hidden layer
        hidden_layer_output = np.dot(self.weights_input_hidden, inputs)
        
        # Apply linear activation function to hidden layer output
        hidden_layer_output = np.maximum(0, hidden_layer_output)
        
        # Compute dot product of hidden layer output and weights from hidden to output layer
        output = np.dot(self.weights_hidden_output, hidden_layer_output)
        
        return output


# Define input vector
input_vector = np.array([0.5, 0.2, 0.1])

# Create multi layer neural network
network = MultiLayerNeuralNetwork(3, 4, 2)

# Compute output of network
output = network.forward(input_vector)
print("Output of network:", output)
