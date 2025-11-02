import matplotlib.pyplot as plt

T = 50000         
m = 1000          
g = 9.81        
t_total = 16    
dt = 1         

time = [0]
velocity = [0]
altitude = [0]

for t in range(1, t_total + 1):
    if t <= 10:
        a = (T/m) - g
    else:
        a = -g

    v_new = velocity[-1] + a * dt
    h_new = altitude[-1] + velocity[-1] * dt

    time.append(t)
    velocity.append(v_new)
    altitude.append(h_new)

max_v = max(velocity)
max_h = max(altitude)
t_vmax = time[velocity.index(max_v)]
t_hmax = time[altitude.index(max_h)]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))

ax1.plot(time, velocity, color='orange')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Velocity (m/s)')
ax1.set_title('Velocity vs Time')
ax1.scatter(t_vmax, max_v, color='red', label='Max Velocity')
ax1.legend()

ax2.plot(time, altitude, color='blue')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Altitude (m)')
ax2.set_title('Altitude vs Time')
ax2.scatter(t_hmax, max_h, color='green', label='Max Altitude')
ax2.legend()

plt.tight_layout()
plt.show()
