import numpy as np
import matplotlib.pyplot as plt

# Set parameters
P_max = 1000 # Pa
tau = 0.1 # s
c = 2500 # m/s

# Create grid of x and t values
x = np.linspace(-10, 10, 1000) # m
x = x - x[int(len(x)/2)] # center x at 0
t = np.array([0, 0.1, 0.2]) # s

# Create meshgrid of x and t values
x_grid, t_grid = np.meshgrid(x, t)

# Calculate pressure pulse at each x and t value
P = P_max * np.exp(-(t_grid/tau)**2) * np.exp(-(x_grid/(2*c*t_grid))**2)

# With no masking and using x vals instead of x_grid vals

# Plot pressure pulse for different times
plt.figure(figsize=(10,5))
plt.subplot(1,3,1)
plt.plot(x, P[:,0], label='t=0s')
plt.title('Pressure Pulse')
plt.xlabel('x (m)')
plt.ylabel('Pressure (Pa)')
plt.ylim([0, 1100])
plt.legend()

plt.subplot(1,3,2)
plt.plot(x, P[:,1])
plt.title('t = 0.1 s')
plt.xlabel('x (m)')
plt.ylim([0, 1100])

plt.subplot(1,3,3)
plt.plot(x, P[:,2])
plt.title('t = 0.2 s')
plt.xlabel('x (m)')
plt.ylim([0, 1100])

plt.show()
