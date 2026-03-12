from simple_pendulum import simulate_simple_pendulum
import matplotlib.pyplot as plt
import numpy as np

for i in range(-5,5):
    theta0 = np.radians(45)  # Initial angle in radians
    if i == 0:
        continue
    omega0 = np.radians(50 * i)  # Initial angular velocity
    df = simulate_simple_pendulum(theta0, omega0)
    plt.plot(df['theta_rad'], df['time'],'.', label=f' {50 * i}°')

plt.xlabel('Angle (radians)')
plt.ylabel('Time (s)')
plt.title('Time vs Angle for Simple Pendulum with Varying Initial Angular Velocity')
plt.grid()
plt.legend()
plt.show()

for i in range(-10,10):
    theta0 = np.radians(100)  # Initial angle in radians
    omega0 = np.radians(100 * i)  # Initial angular velocity
    df = simulate_simple_pendulum(theta0, omega0)
    plt.plot(df['theta_rad'], df['omega'],'.', label=f' {100 * i}°')

plt.xlabel('Angle (radians)')
plt.ylabel('Angular Velocity (rad/s)')
plt.title('Phase Space of Simple Pendulum with Varying Initial Angular Velocity')
plt.grid()
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.show()