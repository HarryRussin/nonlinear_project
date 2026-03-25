from simple_pendulum import simulate_simple_pendulum
import matplotlib.pyplot as plt
import numpy as np
import plot_style  

Amplitudes = np.linspace(0, 2, 1000)
gamma = 0.5
omega_drive = 0.67

for i in Amplitudes:

    A = i   
    df = simulate_simple_pendulum(
        0.0, 0.0,
        gamma=gamma, A_drive=A, omega_drive=omega_drive,
        t_max=1000,
    )

    T_drive    = 2 * np.pi / omega_drive
    time_vals  = df['time'].to_numpy()
    n_max      = int(time_vals[-1] / T_drive)
    sample_times = np.arange(50, n_max + 1) * T_drive
    indices    = np.searchsorted(time_vals, sample_times, side='left')
    indices    = np.unique(np.clip(indices, 0, len(time_vals) - 1))


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