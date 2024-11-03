'''import numpy as np
import scipy.signal

# Input matrix (4x4)
matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

# Kernel (3x3)
k = np.array([
    [1, 0, -1],
    [1, 0, -1],
    [1, 0, -1]
])

# Convolution without padding
nopadding= scipy.signal.convolve2d(matrix, k, mode='valid')
print("Output without padding:")
print(nopadding)

# Convolution with padding
zeropadding = scipy.signal.convolve2d(matrix, k, mode='same')
print("\nOutput with padding:")
print(zeropadding)'''
'''import numpy as np

# Define the sequences x[n] and h[n]
x = np.array([1, 2, 3, 4])
h = np.array([1, 2, 1])
x=[]
l=int(input("enter size of x[n]: "))
h=[]
m=int(input("enter size of h[n]"))
for i in range(l):
    n=input("enter values: ")
    x.append(n)
for i in range(m):
    c=input("enter values: ")
    h.append(c)
def convolve_with_padding(x, h):
    # Calculate the length of the output sequence
    N = l + m - 1
    
    # Zero pad x and h to the length of the output sequence
    x_padded = np.pad(x, (0, N -l), 'constant')
    h_padded = np.pad(h, (0, N -m), 'constant')
    
    print(f"Padded x[n]: {x_padded}")
    print(f"Padded h[n]: {h_padded}")
    
    # Perform convolution
    y = np.convolve(x_padded, h_padded)
    
    # Slice the output to keep only the first N elements
    y = y[:N]
    
    return y

# Perform convolution with zero padding
output = convolve_with_padding(x, h)

# Print the result
print(f"Output y[n]: {output}")
import numpy as np

# Initialize empty lists
x = []
h = []

# Get the size of the sequences from the user
l = int(input("Enter size of x[n]: "))
m = int(input("Enter size of h[n]: "))

# Get values for x[n]
print("Enter values for x[n]:")
for _ in range(l):
    value = int(input())  # Convert input to integer
    x.append(value)

# Get values for h[n]
print("Enter values for h[n]:")
for _ in range(m):
    value = int(input())  # Convert input to integer
    h.append(value)

def convolve_with_padding(x, h):
    # Convert lists to numpy arrays
    x = np.array(x)
    h = np.array(h)
    
    # Calculate the length of the output sequence
    N = len(x) + len(h) - 1
    
    # Zero pad x and h to the length of the output sequence
    x_padded = np.pad(x, (0, N - len(x)), 'constant')
    h_padded = np.pad(h, (0, N - len(h)), 'constant')
    
    print(f"Padded x[n]: {x_padded}")
    print(f"Padded h[n]: {h_padded}")
    
    # Perform convolution
    y = np.convolve(x_padded, h_padded)
    
    # Slice the output to keep only the first N elements
    y = y[:N]
    
    return y

# Perform convolution with zero padding
output = convolve_with_padding(x, h)

# Print the result
print(f"Output y[n]: {output}")'''

