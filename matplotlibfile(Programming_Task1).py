import matplotlib.pyplot as plt
import random
import time

num_points = 40

temperatures = []
voltages = []
currents = []
timestamps = []

for i in range(num_points):
    t = i  
    temperature  = random.uniform(10, 40)   
    voltage = random.uniform(3.0, 5.0) 
    current  = random.uniform(10.0 , 20.0) 
    
    timestamps.append(t)
    temperatures.append(temperature)
    voltages.append(voltage)
    currents.append(current)
    
    time.sleep(0.1)  


plt.figure(figsize=(8, 4))
plt.plot(timestamps, temperatures, label='Temperature (°C)')
plt.plot(timestamps, voltages, label='Voltage (V)')
plt.plot(timestamps, currents, label='Current (A)')

plt.xlabel("Time (s)")
plt.ylabel("Value")
plt.title("CubeSat Telemetry Simulation")
plt.legend()
plt.tight_layout()
plt.show()
