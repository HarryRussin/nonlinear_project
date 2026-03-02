
from rk4 import RK4
import numpy as np
import matplotlib.pyplot as plt






dt = 0.1 #s
t = 0 #s
import numpy as np
import pandas as pd

def simulate_simple_pendulum(theta0, omega0, g=9.81, L=1.0, dt=0.01, t_max=10.0):
    # Simulate a simple pendulum (Euler method)
    t = np.arange(0, t_max + dt, dt)
    theta = np.zeros_like(t)
    omega = np.zeros_like(t)
    theta[0] = theta0
    omega[0] = omega0
    for i in range(len(t) - 1):
        omega[i + 1] = omega[i] - (g / L) * np.sin(theta[i]) * dt
        theta[i + 1] = theta[i] + omega[i + 1] * dt
    return pd.DataFrame({
        'time': t,
        'theta_rad': theta,
        'theta_deg': np.degrees(theta),
        'omega': omega
    })

def zero_crossing_times(theta, time):
    crossings = []
    for i in range(1, len(theta)):
        if theta[i - 1] * theta[i] < 0:  
            t_cross = time[i - 1] - theta[i - 1] * (time[i] - time[i - 1]) / (theta[i] - theta[i - 1])
            crossings.append(t_cross)
    return crossings

for i in range(10):
    theta0 = np.radians(1 * i)  # Initial angle in radians
    omega0 = 0.0  # Initial angular velocity
    df = simulate_simple_pendulum(theta0, omega0)
    plt.plot(df['theta_rad'], df['omega'], label=f'Initial Angle: {1 * i}°')
    # crossings = zero_crossing_times(df['theta_rad'], df['time'])
    # if crossings:
    #     plt.scatter(crossings, [0]*len(crossings), color='red', s=20)  # Mark zero crossings

plt.xlabel('Angle (radians)')
plt.ylabel('Angular Velocity (rad/s)')
plt.title('Phase Space of Simple Pendulum')
plt.grid()
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.show()

for i in range(10):
    theta0 = np.radians(1 * i)  # Initial angle in radians
    omega0 = 0.0  # Initial angular velocity
    df = simulate_simple_pendulum(theta0, omega0)
    plt.plot(df['time'], df['theta_rad'], label=f'Initial Angle: {1 * i}°')
    crossings = zero_crossing_times(df['theta_rad'], df['time'])
    if crossings:
        plt.scatter(crossings, [0]*len(crossings), color='red', s=20)  # Mark zero crossings
plt.xlabel('Time (s)')
plt.ylabel('Angle (radians)')
plt.title('Angle vs Time for Simple Pendulum')
plt.grid()
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.show()