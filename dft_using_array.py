import numpy as np
import matplotlib.pyplot as plt
def DFT(x):
	N=len(x)
	X=np.zeros(N, dtype=complex)
	for k in range(N):
		for n in range(N):
			X[k]+=x[n] *np.exp((-2j *np.pi * k*n)/N)
	return X
x=np.array([1,2,3,4])
X=DFT(x)
plt.figure(figsize=(14,6))
plt.subplot(1,3,1)
plt.stem(np.arange(len(x)),x)
plt.title("Original signal")
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")

plt.subplot (1,3,2)
plt.stem(np.arange(len(X)),np.abs(X))
plt.title("Magnitude of DFT")
plt.xlabel("Frequency Bin")
plt.ylabel("Magnitude")

plt.subplot(1, 3, 3)
plt.stem(np.arange(len(X)), np.angle(X), use_line_collection=True)
plt.title("Phase of DFT")
plt.xlabel("Frequency Bin")
plt.ylabel("Phase (radians)")

plt.tight_layout()
plt.show()



