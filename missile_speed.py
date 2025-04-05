# Author: Ali Mosin Hasan
# Date: 04/04/2025
# Description: This Python program simulates a radar system detecting a missile's speed using the Doppler shift effect. It compares:
#               Actual missile speed (ground truth)
#               Estimated speed based on the Doppler frequency shift detected by the radar

import numpy as np
import matplotlib.pyplot as plt

# Constants
c = 3e8  # Speed of light (m/s)
f_transmit = 10e9  # Radar transmission frequency (Hz)
initial_velocity = 300  # Initial missile velocity (m/s)
acceleration = 10  # Missile acceleration (m/s²)
time_duration = 10  # Total simulation time (seconds)
time_step = 0.1  # Time step for simulation (seconds)

# Time array
time_points = np.arange(0, time_duration, time_step)

# Actual missile velocity (ground truth)
true_velocities = initial_velocity + acceleration * time_points

# Simulated radar measurement (Doppler shift)
measured_doppler_shifts = (2 * true_velocities * f_transmit) / c

# Estimated velocity from Doppler shift
estimated_velocities = (measured_doppler_shifts * c) / (2 * f_transmit)

# Plot results
plt.figure(figsize=(10, 5))

# Plot actual vs estimated velocity
plt.plot(time_points, true_velocities, label="Actual Missile Speed (m/s)", color="b", linestyle="dashed")
plt.plot(time_points, estimated_velocities, label="Radar Estimated Speed (m/s)", color="r")
plt.xlabel("Time (seconds)")
plt.ylabel("Speed (m/s)")
plt.title("Missile Speed Detection Using Radar Doppler Shift")
plt.legend()
plt.grid()

plt.show()
