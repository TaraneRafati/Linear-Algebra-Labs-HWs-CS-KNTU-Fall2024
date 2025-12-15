import timeit
def inverse(A):
    n = len(A)
    if any(len(row) != n for row in A):
        raise ValueError("matrix is not square")
    augmented = [row[:] + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(A)]
    for i in range(n):
        max_row = i
        for k in range(i + 1, n):
            if abs(augmented[k][i]) > abs(augmented[max_row][i]):
                max_row = k
        if max_row != i:
            augmented[i], augmented[max_row] = augmented[max_row], augmented[i]
        pivot = augmented[i][i]
        if pivot == 0:
            raise ValueError("matrix is singular")
        for j in range(2 * n):
            augmented[i][j] /= pivot
        for k in range(n):
            if k != i:
                factor = augmented[k][i]
                for j in range(2 * n):
                    augmented[k][j] -= factor * augmented[i][j]
    inverse_matrix = [row[n:] for row in augmented]
    return inverse_matrix

# test
A = [[4, 7],
    [2, 6]]
t = timeit.timeit(lambda : inverse(A), number=100)
print(t)
B = inverse(A)
print(B)