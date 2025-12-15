import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

A = np.array([[1, 2, 1],
              [2, -1, -1],
              [-1, 1, -2]])

B = np.array([[1, 2, -3],
              [3, 1, 1],
              [2, 1, 0]])

C = np.array([[1, 2, -3],
              [3, 6, -9],
              [-2,-4, 6]])

fig = plt.figure()

############### part one
# matrices = [A, B, C]
# titles = ['Matrix A', 'Matrix B', 'Matrix C']

# for i, M in enumerate(matrices, start=1):
#     ax_row = fig.add_subplot(2, 3, i, projection='3d')
#     ax_row.set_title(f'Row Space of {titles[i-1]}')
    
#     V_row = np.random.randn(200, 3) @ M
#     ax_row.scatter(V_row[:, 0], V_row[:, 1], V_row[:, 2], color='r')
    
#     ax_col = fig.add_subplot(2, 3, i+3, projection='3d')
#     ax_col.set_title(f'Column Space of {titles[i-1]}')
     
#     V_col = M @ np.random.randn(3, 200) 
#     ax_col.scatter(V_col[0, :], V_col[1, :], V_col[2, :], color='b')

############### part two
# matrices = [B, C]
# titles = ['Matrix B', 'Matrix C']

# for i, M in enumerate(matrices):
#     ax = fig.add_subplot(1, 2, i+1, projection='3d')
#     ax.set_title(f'Row and Column Spaces of {titles[i]}')
    
#     V_row = np.random.randn(200, 3) @ M
#     ax.scatter(V_row[:, 0], V_row[:, 1], V_row[:, 2], color='r', label='Row Space')
    
#     V_col = M @ np.random.randn(3, 200)
#     ax.scatter(V_col[0, :], V_col[1, :], V_col[2, :], color='b', label='Column Space')
    
#     ax.legend()

plt.show()