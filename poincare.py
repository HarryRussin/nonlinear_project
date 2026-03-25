
import matplotlib.pyplot as plt
from simple_pendulum import simulate_simple_pendulum
import numpy as np
import plot_style 


def poincare_section(df, omega_drive, skip_periods=50):
    """Sample (theta, omega) once per drive period: t = n * 2*pi/omega_drive."""
    t = df["time"].to_numpy()
    theta = df["theta_rad"].to_numpy()
    omega = df["omega"].to_numpy()

    T_drive = 2 * np.pi / omega_drive
    n_max = int(t[-1] / T_drive)
    n_values = np.arange(skip_periods, n_max + 1)
    sample_times = n_values * T_drive

    # Map each sample time to the nearest simulated timestamp.
    indices = np.searchsorted(t, sample_times, side="left")
    indices = np.clip(indices, 0, len(t) - 1)
    indices = np.unique(indices)

    return theta[indices], omega[indices]

if __name__ == "__main__":

    A_drive = 1.15
    omega_drive = 0.67
    gamma = 0.5
    theta0 = np.radians(0)  # Initial angle in radians
    omega0 = 0  # Initial angular velocity
    df = simulate_simple_pendulum(
        theta0,
        omega0,
        gamma=gamma,
        A_drive=A_drive,
        omega_drive=omega_drive,
        t_max=100000,
    )
    
    theta_poincare, omega_poincare = poincare_section(df, omega_drive)
    
    fig, ax = plt.subplots(figsize=(3.4, 2.8))
    ax.scatter(theta_poincare, omega_poincare,
               s=1.5, c='k', linewidths=0, rasterized=True)
    ax.set_xlabel(r'$\theta$ (rad)')
    ax.set_ylabel(r'$\dot\theta$ (rad s$^{-1}$)')
    ax.text(0.97, 0.96, rf'$A={A_drive},\ \gamma={gamma}$',
            transform=ax.transAxes, ha='right', va='top', fontsize=8)
    plt.tight_layout(pad=0.6)
    plt.show()