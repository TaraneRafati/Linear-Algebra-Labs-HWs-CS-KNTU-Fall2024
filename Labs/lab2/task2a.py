import matplotlib.pyplot as plt
import numpy as np
from face_data import Face1, Face2, Face3, edges

def plot_face(plt,X,edges,color='b'):
    "plots a face"

    plt.plot(X[:,0], X[:,1], 'o', color=color)
    
    for i, j in edges:
        xi = X[i,0]
        yi = X[i,1]

        xj = X[j,0]
        yj = X[j,1]
        
        # draw a line between X[i] and X[j]
        plt.plot((xi,xj), (yi,yj), '-', color=color)
    
    plt.axis('square')
    plt.xlim(-100,100)
    plt.ylim(-100,100)

# plot_face(plt, Face1, edges, color='b')
# plt.show()

fig = plt.figure()

for alpha in np.linspace(0, 1, 20):
    plt.cla()
    face = (1 - alpha) * Face1 + alpha * Face2
    plot_face(plt, face, edges, color='b')
    plt.draw()
    plt.pause(.1)
    
for alpha in np.linspace(0, 1, 20):
    plt.cla()
    face = (1 - alpha) * Face2 + alpha * Face3
    plot_face(plt, face, edges, color='b')
    plt.draw()
    plt.pause(.1)

for alpha in np.linspace(0, 1, 20):
    plt.cla()
    face = (1 - alpha) * Face3 + alpha * Face1
    plot_face(plt, face, edges, color='b')
    plt.draw()
    plt.pause(.1)

plt.show()


# print(edges)