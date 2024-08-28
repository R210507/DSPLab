#dft of audio signal
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Step 1: Load the audio signal
sample_rate, audio_data = wavfile.read('/home/likitha/Downloads/mixkit-small-group-cheer-and-applause-518.wav')

# Step 2: Compute the DFT
dft = np.fft.fft(audio_data)
dft_magnitude = np.abs(dft)

# Step 3: Compute the frequency axis
frequencies = np.fft.fftfreq(len(dft), 1/sample_rate)

# Step 4: Plot the magnitude spectrum
plt.figure(figsize=(12, 6))
plt.plot(frequencies[:len(frequencies)//2], dft_magnitude[:len(dft)//2])
plt.title('Magnitude Spectrum of the Audio Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.show()
