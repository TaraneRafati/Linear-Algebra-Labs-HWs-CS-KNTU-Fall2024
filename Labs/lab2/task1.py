import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

n = 11

S1 = np.vstack((-np.cos(np.linspace(0,np.pi,n)),
                -.7+np.sin(np.linspace(0,np.pi,n)))).T
S2 = np.vstack((np.linspace(-1.2,1.2,n),
                np.zeros(n))).T


rng = np.linspace(0,1.5,20)

for alpha in rng:
    plt.cla()

    S3 = (1 - alpha) * S1 + alpha * S2

    plt.plot(S1[:,0], S1[:,1], 'ro-')
    plt.plot(S2[:,0], S2[:,1], 'ro-')

    plt.plot(S3[:,0], S3[:,1], 'bo-')

    plt.xlim(-2,2)
    plt.ylim(-2,2)

    plt.draw()
    plt.pause(.1)

plt.show()
