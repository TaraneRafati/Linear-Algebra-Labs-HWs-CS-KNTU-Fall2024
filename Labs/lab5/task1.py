import numpy as np
import timeit

A = np.random.rand(100, 200)
d1 = np.random.rand(100).reshape(100, 1)
D1 = np.diag(d1.ravel())

t1 = timeit.timeit(lambda : d1*A, number=10000)
t2 = timeit.timeit(lambda : D1@A, number=10000)

print('d1*A : ', t1)
print('D1@A : ', t2)
