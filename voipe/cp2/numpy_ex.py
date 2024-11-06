import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

x = np.array([1, 3, 4, 5])
A = np.array([[1, 3], [4, 5]])


Z = np.zeros(5)  # [0. 0. 0. 0. 0.]

np.shape(Z)  # (5,)

Z2 = np.zeros((4, 5))

""" 
[[0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]] 
 
"""
np.shape(Z2)  # (4,5)

# Cutting Matrics (indexing)
A = np.array([[1, 2, 3], [4, 5, 6]])

A[0, 0]  # 1
A[0, 1]  # 2

A[:, 0]  # first column, ":"reads all rows
A[0, :]  # first row, ":" reads all columns


x, y = np.meshgrid(np.linspace(-2, 2, 30), np.linspace(-2, 2, 30))
z = np.cos(x**2 + y**2)

fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot_surface(x, y, z)
ax.set_title("Texture")
