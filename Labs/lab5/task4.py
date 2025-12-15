import imageio
import matplotlib.pyplot as plt
import numpy as np

G = imageio.imread('nasir-al-mulk-gray.jpg')
I = imageio.imread('nasir-al-mulk.jpg')
G = np.stack([G] * 3, axis=-1)
print(G.shape)

for alpha in np.linspace(0,1,20):
    J = ((1 - alpha) * G + alpha * I).astype(np.uint8)
    
    plt.imshow(J)
    plt.draw()
    plt.pause(.1)

plt.show()