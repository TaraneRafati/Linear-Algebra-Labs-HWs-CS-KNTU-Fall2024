import numpy as np


# B = A - A.mean(axis=0).reshape((1,A.shape[1]))

l1 = [1,2,3]
l2 = [4,5,6]
a1 = np.array(l1)
a2 = np.array(l2)
print(l1+l2)
print(a1+a2)

a = np.array([1,2,3,4,5,6,7,8,9,10], dtype=np.int64)
b = np.array([1,2,3,4,5,6,7,8,9,10], dtype=np.int32)
c = np.array([1,2,3,4,5,6,7,8,9,10], dtype=np.int16)
d = np.array([1,2,3,4,5,6,7,8,9,10], dtype=np.int8)
e = np.array([1,2,3,4,5,6,7,8,9,10], dtype=np.uint8)
print(a.itemsize, b.itemsize, c.itemsize, d.itemsize, e.itemsize)
print(a.nbytes, b.nbytes, c.nbytes, d.nbytes, e.nbytes)
print(d-4)
print(e-4)

f = np.array([1,2,3,4,5,6,7,8,9,10], dtype=np.float32)
g = np.array([1,2,3,4,5,6,7,8,9,10], dtype=np.float64)
h = np.array([1,2,3,4,5,6,7,8,9,10], dtype=np.float16)
print(f.nbytes, g.nbytes, h.nbytes)

l = np.array([False, True, True])
print(l.dtype)
l = np.array([0, 1, 1], dtype=bool)
print(l.dtype)
print(l.nbytes)

A = np.random.rand(200,10)
mu = np.zeros(A.shape[1])
for i in range(A.shape[0]):
    mu += A[i]
mu /= A.shape[0]
B = np.zeros_like(A)
for i in range(A.shape[0]):
    B[i] = A[i] - mu
print(B)
