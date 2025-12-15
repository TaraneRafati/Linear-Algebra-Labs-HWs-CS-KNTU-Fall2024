import timeit
def solve_equations(A, b):
    n = len(A)
    if any(len(row) != n for row in A):
        raise ValueError("matrix is not square")
    augmented = [row[:] + [b[i]] for i, row in enumerate(A)]
    for i in range(n):
        max_row = i
        for k in range(i + 1, n):
            if abs(augmented[k][i]) > abs(augmented[max_row][i]):
                max_row = k
        if max_row != i:
            augmented[i], augmented[max_row] = augmented[max_row], augmented[i]
        if augmented[i][i] == 0:
            raise ValueError("matrix is singular")
        pivot = augmented[i][i]
        augmented[i] = [x / pivot for x in augmented[i]]
        for j in range(i + 1, n):
            factor = augmented[j][i]
            augmented[j] = [augmented[j][k] - factor * augmented[i][k] for k in range(len(augmented[i]))]
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = augmented[i][-1] - sum(augmented[i][j] * x[j] for j in range(i + 1, n))
    return x

# test
A = [[2, 1, -1],
     [-3, -1, 2],
     [-2, 1, 2]]
b = [8, -11, -3]
t = timeit.timeit(lambda : solve_equations(A, b), number=100)
print(t)
x = solve_equations(A, b)
print(x)