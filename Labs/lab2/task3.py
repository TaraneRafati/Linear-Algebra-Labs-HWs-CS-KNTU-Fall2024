import numpy as np

m,n = 20,10
A = np.random.rand(m,n)
u = np.random.rand(n)

v = np.sum(A * u, axis=1)

v1 = np.zeros(m)
for i in range(n):
    v1 += A[:,i] * u[i]

print(v == v1)