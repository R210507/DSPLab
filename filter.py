import numpy as np
import matplotlib.pyplot as plt

# Step 1: Take inputs for multiple zeros from the user
num_zeros = int(input("Enter the number of zeros: "))

zeros = []
for i in range(num_zeros):
    r = float(input(f"Enter the distance of zero {i+1} (r) from the origin: "))
    w = float(input(f"Enter the angular distance of zero {i+1} (w in radians): "))
    zx = r * np.exp(1j * w)  # Compute zero in complex form
    zeros.append(zx)

# Step 2: Define the combined frequency response H(z)
def H(zeros, omega):
    H_w = np.ones_like(omega, dtype=complex)  # Initialize as 1 for multiplication
    for z in zeros:
        H_w *= (omega - z)  # Each zero contributes to the frequency response
    return H_w

# Step 3: Compute the frequency response over a range of frequencies
omega = np.linspace(-np.pi, np.pi, 1000)  # Frequency range from -π to π
H_w = H(zeros, r * np.exp(1j * omega))  # Compute the frequency response
magnitude_spectrum = np.abs(H_w)  # Magnitude of H(omega)
phase_spectrum = np.angle(H_w)  # Phase of H(omega)

# Step 4: Plot the zeros on the complex plane, the magnitude spectrum, and the phase spectrum
plt.figure(figsize=(12, 10))

# Subplot 1: Plot the zeros on the complex plane
plt.subplot(3, 1, 1)
for z in zeros:
    plt.plot(np.real(z), np.imag(z), 'bo')  # Plot each zero
plt.title("Zeros on Complex Plane")
plt.xlabel("Real Part")
plt.ylabel("Imaginary Part")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)

# Subplot 2: Plot the magnitude spectrum
plt.subplot(3, 1, 2)
plt.plot(omega, magnitude_spectrum)
plt.title("Combined Magnitude Spectrum of Zeros")
plt.xlabel("Frequency (ω in radians)")
plt.ylabel("Magnitude |H(ω)|")
plt.grid(True)

# Subplot 3: Plot the phase spectrum
plt.subplot(3, 1, 3)
plt.plot(omega, phase_spectrum)
plt.title("Combined Phase Spectrum of Zeros")
plt.xlabel("Frequency (ω in radians)")
plt.ylabel("Phase (radians)")
plt.grid(True)

plt.tight_layout()
plt.show()
