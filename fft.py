import numpy as np
import matplotlib.pyplot as plt

# Function to generate a sample signal (sine wave)
def generate_signal(frequency, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = np.sin(2 * np.pi * frequency * t)
    return t, signal

# Function to create an exponentially decreasing signal
def exponential_decay(t, decay_rate):
    return np.exp(-decay_rate * t)

# Function to compute the magnitude spectrum
def magnitude_spectrum(signal, sample_rate):
    spectrum = np.fft.fft(signal)
    magnitude = np.abs(spectrum)
    freq = np.fft.fftfreq(len(signal), 1/sample_rate)
    return freq, magnitude

# Parameters
frequency = 5  # Frequency of the sine wave in Hz
duration = 2   # Duration in seconds
sample_rate = 100  # Samples per second
decay_rate = 1  # Decay rate for the exponential signal

# Generate the signal
t, signal = generate_signal(frequency, duration, sample_rate)

# Generate the exponentially decreasing signal
decay_signal = exponential_decay(t, decay_rate)

# Multiply the original signal by the exponentially decreasing signal
modulated_signal = signal * decay_signal

# Compute the magnitude spectrum
freq, magnitude = magnitude_spectrum(modulated_signal, sample_rate)

# Plot the original and modulated signals
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, signal, label='Original Signal (Sine Wave)')
plt.plot(t, modulated_signal, label='Modulated Signal', alpha=0.7)
plt.title('Time Domain Signals')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()

# Plot the magnitude spectrum
plt.subplot(2, 1, 2)
plt.plot(freq[:len(freq)//2], magnitude[:len(magnitude)//2])
plt.title('Magnitude Spectrum')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude')
plt.xlim(0, 20)  # Adjust x-axis limit as needed
plt.grid()

plt.tight_layout()
plt.show()
