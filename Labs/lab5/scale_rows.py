import numpy as np
import timeit

d1 = np.array([2,3,4]).reshape((3,1))

A = np.array([[1,1,1,1],
              [1,2,2,2],
              [1,2,3,4]])

print('d1=\n', d1)
print('A=\n', A)

print('d1.shape=\n', d1.shape)
print('A.shape=\n', A.shape)

print('d1 * A= \n', d1 * A)

# Q1
print('# Q1')
d2 = np.array([10,20,30,40])
print('d2.shape=\n', d2.shape)
print('d2 * A =\n', d2 * A)

# Q2
print('# Q2')
D1 = np.diag(d1.ravel())

t1 = timeit.timeit(lambda : d1*A, number=100000)/100
t2 = timeit.timeit(lambda : D1@A, number=100000)/100

print('d1*A : ', t1)
print('D1@A : ', t2)
