# Author: Riley Sweeting
# Description: This file is used for practicing my Matplotlib skills, and contains example plots and visuals for future reference.

# Import NumPy & MatPlotLib packages
import numpy as np
import matplotlib as mlp
import matplotlib.pyplot as plt

# Use Numpy to randomly generate sample data and labels
x = np.random.rand(15,2) # Uniform distribution of floats between 0-1 of shape 15x2
y = np.random.randint(0, 3, size=15) # Uniform distribution of 15 0's and 1's (ints)

# Plot a scatterplot
plt.scatter(x[:, 0], x[:, 1], c=y, cmap='Set3')
plt.title('Sample Scatter Plot')
plt.xlabel('X1')
plt.ylabel('X2')
plt.show()