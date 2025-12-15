import timeit
import numpy as np
from numba import jit, prange
@jit(nopython=True)
def solve_equations(A, b):
    n = len(A)
    for i in prange(n):
        if len(A[i]) != n:
            raise ValueError("matrix is not square")
    augmented = np.zeros((n, n + 1), dtype=np.float64)
    for i in range(n):
        augmented[i, :n] = A[i, :]
        augmented[i, n] = b[i]
    for i in range(n):
        max_row = i
        for k in prange(i + 1, n):
            if abs(augmented[k, i]) > abs(augmented[max_row, i]):
                max_row = k
        if max_row != i:
            augmented[i, :], augmented[max_row, :] = augmented[max_row, :].copy(), augmented[i, :].copy()
        if augmented[i, i] == 0:
            raise ValueError("matrix is singular")
        pivot = augmented[i, i]
        augmented[i, :] /= pivot
        for j in prange(i + 1, n):
            factor = augmented[j, i]
            augmented[j, :] -= factor * augmented[i, :]
    x = np.zeros(n, dtype=np.float64)
    for i in prange(n - 1, -1, -1):
        x[i] = augmented[i, n] - np.dot(augmented[i, i + 1:n], x[i + 1:n])
    return x

# test
A = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]], dtype=np.float64)
b = np.array([8, -11, -3], dtype=np.float64)
t = timeit.timeit(lambda : solve_equations(A, b), number=1)
t = timeit.timeit(lambda : solve_equations(A, b), number=100)
print(t)
x = solve_equations(A, b)
print(x)
################################################################
@jit(nopython=True)
def inverse(A):
    n = len(A)
    for i in prange(n):
        if len(A[i]) != n:
            raise ValueError("matrix is not square")
    augmented = np.zeros((n, 2 * n), dtype=np.float64)
    for i in prange(n):
        augmented[i, :n] = A[i, :]
        augmented[i, n + i] = 1.0
    for i in range(n):
        max_row = i
        for k in prange(i + 1, n):
            if abs(augmented[k, i]) > abs(augmented[max_row, i]):
                max_row = k
        if max_row != i:
            augmented[i, :], augmented[max_row, :] = augmented[max_row, :].copy(), augmented[i, :].copy()
        pivot = augmented[i, i]
        if pivot == 0:
            raise ValueError("matrix is singular")
        augmented[i, :] /= pivot
        for k in prange(n):
            if k != i:
                factor = augmented[k, i]
                augmented[k, :] -= factor * augmented[i, :]
    inverse_matrix = augmented[:, n:]
    return inverse_matrix

# test
A = np.array([[4, 7],
              [2, 6]])
t = timeit.timeit(lambda : inverse(A), number=1)
t = timeit.timeit(lambda : inverse(A), number=100)
print(t)
B = inverse(A)
print(B)