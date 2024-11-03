#effect of zero on frequency response of the system
import numpy as np 
import matplotlib.pyplot as plt
def conv_z_to_w(z,P):
	h_w=[]
	for w in P:
		h_w.append((1-(z*np.exp(-1j*w))))
	return h_w
print("Enter Zero parameters")
r_mag=int(input("enter the magnitude of the zero"))
w_phase=int(input("enter the angle at which zero is located"))
z=r_mag*np.exp(1j*r_mag)
P=np.arange(-np.pi,np.pi,0.0001*np.pi)
h_w=conv_z_to_w(z,P)
mag=np.abs(h_w)
phase=np.angle(h_w)
plt.subplot(2,1,1)
plt.plot(P,mag)
plt.xlabel("w axis")
plt.ylabel("mag")
plt.title("magnitude plot")
plt.subplot(2,1,2)
plt.plot(P,phase)
plt.xlabel("w axis")
plt.ylabel("phase")
plt.title("phase plot")
plt.show()
