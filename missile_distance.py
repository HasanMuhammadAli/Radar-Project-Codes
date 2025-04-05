# Author: Ali Mosin Hasan
# Date: 05/04/2025
# Description: This Python simulation models a missile approaching a radar station, 
#              calculating its distance and Doppler frequency shift over time. 
#              The simulation uses classical physics and radar principles #              to visualize how a moving object affects the radar signal.


import numpy as np
import matplotlib.pyplot as plt

# Constants
c = 3e8  # Speed of light (m/s)
f_transmit = 10e9  # Radar transmission frequency (Hz)
initial_velocity = 300  # Initial missile velocity (m/s)
acceleration = 10  # Missile acceleration (m/s²)
initial_distance = 50000  # Initial distance from radar (m)
time_duration = 10  # Total simulation time (seconds)
time_step = 0.1  # Time step for simulation (seconds)

# Time array
time_points = np.arange(0, time_duration, time_step)

# Velocity calculation over time (v = v0 + at)
velocities = initial_velocity + acceleration * time_points

# Distance calculation over time (d = d0 + v0*t + 0.5*a*t^2)
distances = initial_distance - (initial_velocity * time_points + 0.5 * acceleration * time_points**2)

# Doppler shift calculations
doppler_shifts = (2 * velocities * f_transmit) / c

# Plot results
plt.figure(figsize=(12, 6))

# Subplot 1: Distance vs Time
plt.subplot(2, 1, 1)
plt.plot(time_points, distances, label="Missile Distance from Radar (m)", color="b")
plt.xlabel("Time (seconds)")
plt.ylabel("Distance (m)")
plt.title("Missile Distance Over Time")
plt.legend()
plt.grid()

# Subplot 2: Doppler Shift vs Time
plt.subplot(2, 1, 2)
plt.plot(time_points, doppler_shifts, label="Doppler Shift (Hz)", color="r")
plt.xlabel("Time (seconds)")
plt.ylabel("Doppler Frequency Shift (Hz)")
plt.title("Doppler Shift Over Time")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
