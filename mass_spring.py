from rk4 import RK4
import numpy as np
import matplotlib.pyplot as plt

dt = 0.01 #s
t = 0 #s
m = 1 #kg
k = 1 #N/m

period = 2*np.pi*np.sqrt(m/k)
T_10 = 10*period
steps = int(T_10/dt)
times = np.arange(0, T_10, steps)
positions = np.zeros(steps)
velocities = np.zeros(steps)

def ODE(t,y):
    x = y[0]
    v = y[1]
    dxdt = v
    dvdt = -k*x/m
    return np.asarray([dxdt, dvdt])

y = np.asarray([1,0])

for t in times:
    y = RK4(t,y,ODE,dt)
    positions[int(t/dt)] = y[0]
    velocities[int(t/dt)] = y[1]

plt.plot(times, positions)
plt.plot(times, velocities)

plt.title('Mass-Spring System')
plt.grid()
plt.show()
