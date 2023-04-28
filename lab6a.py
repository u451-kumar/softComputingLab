
import numpy as np

def tanh(x):
    return (np.exp(x) - np.exp(-x))/(np.exp(x) + np.exp(-x))
 
x = 1.0
print('Applying Relu on (%.1f) gives %.1f' % (x, tanh(x)))
x = -10.0
print('Applying Relu on (%.1f) gives %.1f' % (x, tanh(x)))
x = 0.0
print('Applying Relu on (%.1f) gives %.1f' % (x, tanh(x)))
x = 15.0
print('Applying Relu on (%.1f) gives %.1f' % (x, tanh(x)))
x = -20.0
print('Applying Relu on (%.1f) gives %.1f' % (x, tanh(x)))