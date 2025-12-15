import imageio
import matplotlib.pyplot as plt

I = imageio.imread('nasir-al-mulk-gray.jpg')

print('I=\n', I)
print('I.dtype= ', I.dtype)
print('I.shape= ', I.shape)
print('num pixles= ', I.shape[0] * I.shape[1])

plt.imshow(I, cmap='gray')
plt.show()

plt.imshow(I.T, cmap='gray')
plt.show()

# plt.imshow(I[100:400, 300:600], cmap='gray')
# plt.show()
