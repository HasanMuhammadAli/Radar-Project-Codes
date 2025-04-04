# Doppler Shift Calculation for a Moving Object
# Author: Ali Mosin Hasan
# Date: 03/04/2025
# Description: This program calculates the Doppler frequency shift
#              when an object moves towards a radar system.

# Constants
c = 3e8  # Speed of light in meters per second (m/s)
f_transmit = 10e9  # Radar transmitted frequency in Hz (10 GHz)

def doppler_shift(velocity):
    """
    Calculates the Doppler shift frequency due to a moving object.
    
    Parameters:
    velocity (float): The speed of the object in meters per second (m/s).
    
    Returns:
    float: The Doppler shift in frequency (Hz).
    """
    return (2 * velocity * f_transmit) / c

# Example: Object moving towards the radar at 50 m/s
velocity = 50  # Velocity of the moving object in m/s
doppler_frequency = doppler_shift(velocity)

# Output the result
print(f"Doppler Shift: {doppler_frequency:.2f} Hz")
