import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt

# Constants
c = 3e8  # Speed of light (m/s)

def calculate_doppler():
    try:
        # Get user input
        f_transmit = float(frequency_entry.get()) * 1e9  # Convert GHz to Hz
        velocity = float(velocity_entry.get()) / 86400  # Convert m/day to m/s

        # Calculate Doppler shift
        doppler_shift = (2 * velocity * f_transmit) / c

        # Display result
        result_label.config(text=f"Doppler Shift: {doppler_shift:.2f} Hz")

        # Generate time data
        time_duration = 10  # Simulate 10 days
        time_step = 1  # 1-day interval
        time_points = np.arange(0, time_duration, time_step)

        # Simulate glacier velocity (constant for now)
        velocities = np.full_like(time_points, velocity * 86400)  # Convert back to m/day

        # Doppler shift over time
        doppler_shifts = (2 * velocities * f_transmit) / c

        # Plot results
        plt.figure(figsize=(10, 5))
        plt.subplot(2, 1, 1)
        plt.plot(time_points, velocities, label="Glacier Speed (m/day)", color="b")
        plt.xlabel("Time (days)")
        plt.ylabel("Speed (m/day)")
        plt.title("Glacier Movement Over Time")
        plt.legend()
        plt.grid()

        plt.subplot(2, 1, 2)
        plt.plot(time_points, doppler_shifts, label="Doppler Shift (Hz)", color="r")
        plt.xlabel("Time (days)")
        plt.ylabel("Doppler Shift (Hz)")
        plt.title("Doppler Shift Over Time")
        plt.legend()
        plt.grid()

        plt.tight_layout()
        plt.show()

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

# Create main window
root = tk.Tk()
root.title("Glacier Radar Sounding Simulation")
root.geometry("400x300")

# Labels and input fields
tk.Label(root, text="Radar Frequency (GHz):").pack(pady=5)
frequency_entry = tk.Entry(root)
frequency_entry.pack()

tk.Label(root, text="Glacier Speed (m/day):").pack(pady=5)
velocity_entry = tk.Entry(root)
velocity_entry.pack()

# Button to calculate
calculate_button = tk.Button(root, text="Calculate Doppler Shift", command=calculate_doppler)
calculate_button.pack(pady=10)

# Label to display result
result_label = tk.Label(root, text="Doppler Shift: -- Hz", font=("Arial", 12))
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
