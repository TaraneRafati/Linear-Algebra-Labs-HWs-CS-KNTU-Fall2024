import scipy.io.wavfile

sampling_rate, data = scipy.io.wavfile.read('voice1.wav')

scipy.io.wavfile.write('output2.wav', sampling_rate*2, data)
scipy.io.wavfile.write('output3.wav', sampling_rate//2, data)
