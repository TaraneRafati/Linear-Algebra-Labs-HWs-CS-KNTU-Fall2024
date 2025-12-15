import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# create a 3 x 2 matrix
A = np.array([[1, 2],
              [3, 6],
              [-2,-4]])


fig = plt.figure()

# A 1 by 2 subplot grid, subplot 1 (3D)
ax1 = fig.add_subplot(1,2,1, projection='3d')
ax1.set_title('column space')

v = A @ np.random.randn(2, 200)
ax1.scatter(v[0,:], v[1,:], v[2,:], color='b')


# A 1 by 2 subplot grid, subplot 2 (2D)
ax2 = fig.add_subplot(1,2,2)
ax2.set_title('row space')

v = np.random.randn(200, 3) @ A
ax2.plot(v[:,0], v[:,1], 'ro')

plt.show()