import imageio
import matplotlib.pyplot as plt
import numpy as np

I = imageio.imread('nasir-al-mulk-gray.jpg')
I = np.hstack((np.vstack((I, I[::-1, :])), np.vstack((I[:, ::-1], I[::-1, ::-1])))) 
plt.imshow(I, cmap='gray')
plt.show()