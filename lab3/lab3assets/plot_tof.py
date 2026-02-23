import matplotlib.pyplot as plt
import numpy as np

# Data
actual_dist = np.array([200, 300, 500, 600, 1200])
s1_dist = np.array([204, 308, 506, 610, 1209])
s2_dist = np.array([197, 294, 492, 593, 1192])

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(actual_dist, s1_dist, marker='o', label='Sensor 1 (0x30)', linestyle='-', color='b')
plt.plot(actual_dist, s2_dist, marker='x', label='Sensor 2 (0x29)', linestyle='--', color='r')
plt.plot(actual_dist, actual_dist, marker='', label='Ideal (Slope=1)', linestyle=':', color='g')

plt.title('Actual vs Measured Distance (Short Mode)')
plt.xlabel('Ground Truth (Actual Distance in mm)')
plt.ylabel('Measured Distance (mm)')
plt.legend()
plt.grid(True)

# Save plot
plt.savefig('/Users/immanuelkoshy/Documents/fastrobogit/lab3/lab3assets/tof_linearity.png')
print("Plot saved to tof_linearity.png")
