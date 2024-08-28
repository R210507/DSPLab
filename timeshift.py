import numpy as np
import matplotlib.pyplot as plt

def dtft(x, w):
    return np.sum(x * np.exp(-1j * w * np.arange(len(x))))

x = np.array([1, 2, 3, 4, 5])
time_shift = 2
x_shifted = np.roll(x, time_shift)
w = np.linspace(0, 2 * np.pi, 100)

X = np.array([dtft(x, wi) for wi in w])
X_shifted = np.array([dtft(x_shifted, wi) for wi in w])

X_expected = X * np.exp(-1j * w * time_shift)

# Plot the results
plt.plot(np.abs(X), label='Original')
plt.plot(np.abs(X_shifted), label='Shifted')
plt.plot(np.abs(X_expected), label='Expected')
plt.legend()
plt.show()
