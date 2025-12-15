import numpy as np
import scipy.io.wavfile
import matplotlib.pyplot as plt

sampling_rate, data = scipy.io.wavfile.read('voice1.wav')
N, no_channels = data.shape
data_reversed = data[::-1]

scipy.io.wavfile.write('output4.wav', sampling_rate, data_reversed)

# optional
plt.plot(np.arange(N), data_reversed)
plt.show()