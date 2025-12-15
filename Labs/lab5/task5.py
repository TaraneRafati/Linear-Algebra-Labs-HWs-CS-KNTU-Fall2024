import imageio
import matplotlib.pyplot as plt
import numpy as np

I = imageio.imread('nasir-al-mulk.jpg')

for alpha in np.linspace(0, np.pi, 100):
    multipliers = np.array([
        np.abs(np.sin(alpha)),
        np.abs(np.sin(alpha + np.pi/4)),
        np.abs(np.sin(alpha + np.pi/2))
    ]).reshape(1, 1, 3)

    J = (I * multipliers).astype(np.uint8)
    plt.imshow(J)
    plt.draw()
    plt.pause(.1)

plt.show()
