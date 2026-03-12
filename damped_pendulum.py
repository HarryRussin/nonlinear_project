from simple_pendulum import simulate_simple_pendulum
import matplotlib.pyplot as plt
import numpy as np

for i in range(1):
    theta0 = np.radians(15)  # Initial angle in radians
    omega0 = 0  # Initial angular velocity
    df = simulate_simple_pendulum(theta0, omega0, gamma=0.1*(i+1))
    plt.plot(df['time'], df['theta_rad'], label=f'Initial Angle: {15}°')

plt.xlabel('Angle (radians)')
plt.ylabel('Time (s)')
plt.title('Time vs Angle for Damped Simple Pendulum')
plt.grid()
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.show()