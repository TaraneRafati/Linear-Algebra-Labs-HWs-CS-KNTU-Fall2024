import numpy as np
import timeit

m,n,p = 100, 50, 2000

A = np.random.rand(m,n,p) 
s = np.random.rand(p)

def with_loop(A, s):
    for i in range(len(s)):
        A[:,:,i] *= s[i]
    return A

def without_loop(A, s):
    # A *= s[np.newaxis, np.newaxis, :]
    # A *= s.reshape((1, 1, p))
    A *= s
    return A 

print('loop   : ', timeit.timeit(lambda: with_loop(np.copy(A), s), number=10000)/100)
print('no loop: ', timeit.timeit(lambda: without_loop(np.copy(A), s), number=10000)/100)

