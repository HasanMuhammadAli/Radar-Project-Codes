#Frequency shift by moving object

c = 3e8 #speed of light
f_transmit = 10e9 #Radar frequency 10GHz
def doppler_shift(velocity):
    return (2*velocity*f_transmit)/c
velocity = 30 #Assume the object is moving towards radar m/s
doppler_frequency = doppler_shift(velocity)
print(f"Doppler Shift: {doppler_frequency:.2f} Hz")