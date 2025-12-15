import numpy as np
import matplotlib.pyplot as plt
from face_data import Face1, edges

def plot_face(plt, X, edges, color='b'):
    "plots a face"
    plt.plot(X[:, 0], X[:, 1], 'o', color=color)

    for i, j in edges:
        xi, yi = X[i]
        xj, yj = X[j]
        
        plt.plot((xi, xj), (yi, yj), '-', color=color)
        
    plt.axis('square')
    plt.xlim(-100, 100)
    plt.ylim(-100, 100)


fig = plt.figure()

#################### A
# for th in np.linspace(0, 2 * np.pi, 100):
#     A = np.array([[np.cos(th), np.sin(th)],
#                   [-np.sin(th), np.cos(th)]])
#     # X = Face1 @ A 
#     X = A @ Face1.T
#     X = X.T
#     plt.cla()
#     plot_face(plt, X, edges, color='b')
#     plt.draw()
#     plt.pause(0.1)

#################### B
# for alpha in np.linspace(-3/4, 4/3, 100):
#     A = np.array([[alpha, 0],
#                   [0, alpha]])
#     X = Face1 @ A 
#     plt.cla() 
#     plot_face(plt, X, edges, color='b') 
#     plt.draw()
#     plt.pause(0.1)

#################### C
# for alpha in np.linspace(3/4, 4/3, 100):
#     beta = 1/alpha
#     A = np.array([[alpha, 0],
#                   [0, beta]])
#     X = Face1 @ A 
#     plt.cla() 
#     plot_face(plt, X, edges, color='b') 
#     plt.draw()
#     plt.pause(0.1)

#################### D
for s in np.linspace(-.7, .7, 100):
    A = np.array([[1, 0],
                  [s, 1]])
    # X = Face1 @ A 
    X = A @ Face1.T
    X = X.T
    plt.cla() 
    plot_face(plt, X, edges, color='b') 
    plt.draw()
    plt.pause(0.1)
#     print(Face1)
#     print(A)
#     print(X)


# plt.show() 
