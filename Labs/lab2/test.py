# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# # plot multiple points
# u = np.array([1,2,3])
# v = np.array([2, 0, -2])

# xs = [u[0], v[0]]
# ys = [u[1], v[1]]
# zs = [u[2], v[2]]

# # base of the vectors set to the origin
# tail_x = [0,0]
# tail_y = [0,0]
# tail_z = [0,0]

# ax.set_xlim(-3,3)
# ax.set_ylim(-3,3)
# ax.set_zlim(-3,3)

# ax.quiver(tail_x, tail_y, tail_z, xs, ys, zs, color='r')

# for i in range(200):
#     a,b = np.random.randn(2)
#     w = a * u + b * v
#     ax.scatter(w[0], w[1], w[2], color='b')

# plt.show()

# # Animating a plot
import matplotlib.pyplot as plt
import numpy as np
from face_data import Face1, Face2, Face3, TargetFace1, TargetFace2, edges


# Function to plot the face
def plot_face(plt, X, edges, color='b'):
    plt.plot(X[:, 0], X[:, 1], 'o', color=color)
    for i, j in edges:
        xi, yi = X[i]
        xj, yj = X[j]
        plt.plot((xi, xj), (yi, yj), '-', color=color)
    plt.axis('square')
    plt.xlim(-100, 100)
    plt.ylim(-100, 100)

# Error function
def calculate_error(F, TargetFace):
    return np.sum((F - TargetFace) ** 2)

# Optimize weights to minimize error
def optimize_weights(Face1, Face2, Face3, TargetFace, edges):
    a, b, c = 1/3, 1/3, 1/3  # Initial guess
    step_size = 0.01  # Step size for weight adjustment
    best_error = float('inf')

    for _ in range(1000):  # Iterations
        # Compute new face F
        F = a * Face1 + b * Face2 + c * Face3
        error = calculate_error(F, TargetFace)
        
        if error < best_error:
            best_error = error
        else:
            # Adjust weights slightly to improve alignment
            a += np.random.uniform(-step_size, step_size)
            b += np.random.uniform(-step_size, step_size)
            c += np.random.uniform(-step_size, step_size)
            a, b, c = max(0, a), max(0, b), max(0, c)  # Keep weights positive

    return a, b, c, F

# Plot faces
plot_face(plt, TargetFace1, edges, color='r')
a, b, c, F = optimize_weights(Face1, Face2, Face3, TargetFace1, edges)
plot_face(plt, F, edges, color='g')

plt.show()

print(f'Optimized weights: a={a:.2f}, b={b:.2f}, c={c:.2f}')
