""" 
Look for a command from the numpy documentation (or elsewhere on the Internet) to calculate the matrix determinant. The determinant is a number that does not require a deeper understanding here. Calculate the determinants of the matrices A, B and AB, where

A=\begin{pmatrix}
1&2\\
3&4
\end{pmatrix}{,} 

B=\begin{pmatrix}
-1  & 1\\
5 & 7
\end{pmatrix}

and AB stands for matrix product. State that det (AB) = det (A) det (B) can be understood as the product of the numbers (the rounding error can be ignored).
"""

import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[-1, 1], [5, 7]])

det_A = np.linalg.det(A)
det_B = np.linalg.det(B)

AB = np.dot(A, B)

det_AB = np.linalg.det(AB)
print(f"det(AB) = {det_AB}")

product_of_dets = det_A * det_B
print(f"det(A) * det(B) = {product_of_dets}")
