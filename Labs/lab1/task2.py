import numpy as np
import scipy.io.wavfile
import matplotlib.pyplot as plt

sampling_rate, data = scipy.io.wavfile.read('voice1.wav')
N, no_channels = data.shape 
channel0 = data[:,0]
channel1 = data[:,1]

# plt.plot(np.arange(N), channel0)
# plt.plot(np.arange(N), channel1)
# plt.show()

# plt.plot(np.arange(N), data)
# plt.show()

sampling_rate_output, data_output = scipy.io.wavfile.read('output1.wav')
plt.plot(np.arange(N), data_output)
plt.show()