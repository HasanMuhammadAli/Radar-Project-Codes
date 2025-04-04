# Author: Ali Mosin Hasan
# Date: 04/04/2025
# Description: This program calculates the Doppler frequency shifts 
#              when an object moves towards a radar system with acceleration.

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

# Velocity over time (assuming constant acceleration)
velocities = initial_velocity + acceleration * time_points

# Doppler shift calculations
doppler_shifts = (2 * velocities * f_transmit) / c

# Plot results
plt.figure(figsize=(10, 5))
plt.plot(time_points, doppler_shifts, label="Doppler Shift (Hz)", color="r")
plt.xlabel("Time (seconds)")
plt.ylabel("Doppler Frequency Shift (Hz)")
plt.title("Doppler Shift Simulation for a Moving Missile")
plt.legend()
plt.grid()
plt.show()
