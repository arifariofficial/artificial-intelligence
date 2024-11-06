""" 
Calculate the inverse matrix of matrix A and  check with the matrix product that both A A^{- 1} and A^{- 1} A produce a unit matrix with ones in diagonals and zeros elsewhere (the values will not be exactly 1 and 0 due to floating point error).

A=\begin{pmatrix}
1&2&3\\
0&1&4\\
5&6&0
\end{pmatrix}
"""

import numpy as np

A = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])

A_inv = np.linalg.inv(A)

# Calculate A * A_inv and A_inv * A
A_A_inv = np.dot(A, A_inv)
A_inv_A = np.dot(A_inv, A)
