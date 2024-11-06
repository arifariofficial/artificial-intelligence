""" 
Draw the lines

y = 2x + 1,
y = 2x + 2,
y = 2x + 3
in the same figure.

Use different drawing colors and line types for your graphs to make them stand out in black and white. Set the image title and captions for the horizontal and vertical axes.
"""

import matplotlib.pyplot as plt
import numpy as np

# Define the range of x values
x = np.linspace(-10, 10, 400)

# Define the equations for y based on x
y1 = 2 * x + 1
y2 = 2 * x + 2
y3 = 2 * x + 3

# Plot each line with a unique line style

plt.plot(x, y1, linestyle="-", color="black", label="y = 2x + 1")
plt.plot(x, y2, linestyle="--", color="blue", label="y = 2x + 2")
plt.plot(x, y3, linestyle="-.", color="red", label="y = 2x + 3")

# Set title and axis lable
plt.title("Grap of y = 2x + 1, y = 2x + 2, y = 2x + 3 ")
plt.xlabel("x-axis")
plt.ylabel("y-axis")


plt.legend()
plt.show()
