import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plot_style  # noqa: F401 — sets rcParams
from numba import njit


dt = 0.1  # s
t = 0  # s

@njit(cache=True)
def _simulate_simple_pendulum_arrays(
    theta0,
    omega0,
    g=1.0,
    L=1.0,
    dt=0.01,
    t_max=50.0,
    gamma=0.0,
    A_drive=0.0,
    omega_drive=0.0,
):
    # Simulate a simple pendulum using RK4 on state y=[theta, omega]
    t = np.arange(0, t_max + dt, dt)
    theta = np.zeros_like(t)
    omega = np.zeros_like(t)
    theta[0] = theta0
    omega[0] = omega0

    th = theta0
    om = omega0
    for i in range(len(t) - 1):
        ti = t[i]

        # inline RK4 so that numba can combile JIT
        k1_theta = om
        k1_omega = -(g / L) * np.sin(th) - gamma * om + A_drive * np.sin(omega_drive * ti)

        th2 = th + 0.5 * dt * k1_theta
        om2 = om + 0.5 * dt * k1_omega
        t2 = ti + 0.5 * dt
        k2_theta = om2
        k2_omega = -(g / L) * np.sin(th2) - gamma * om2 + A_drive * np.sin(omega_drive * t2)

        th3 = th + 0.5 * dt * k2_theta
        om3 = om + 0.5 * dt * k2_omega
        t3 = ti + 0.5 * dt
        k3_theta = om3
        k3_omega = -(g / L) * np.sin(th3) - gamma * om3 + A_drive * np.sin(omega_drive * t3)

        th4 = th + dt * k3_theta
        om4 = om + dt * k3_omega
        t4 = ti + dt
        k4_theta = om4
        k4_omega = -(g / L) * np.sin(th4) - gamma * om4 + A_drive * np.sin(omega_drive * t4)

        th = th + (dt / 6.0) * (k1_theta + 2.0 * k2_theta + 2.0 * k3_theta + k4_theta)
        om = om + (dt / 6.0) * (k1_omega + 2.0 * k2_omega + 2.0 * k3_omega + k4_omega)

        theta[i + 1] = th
        omega[i + 1] = om
        theta[i + 1] = (theta[i + 1] + np.pi) % (2 * np.pi) - np.pi
    return t, theta, omega

def simulate_simple_pendulum(
    theta0,
    omega0,
    g=1.0,
    L=1.0,
    dt=0.01,
    t_max=50.0,
    gamma=0.0,
    A_drive=0.0,
    omega_drive=0.0,
):
    # Build pandas DataFrame outside JIT; Numba handles only numeric arrays.
    t, theta, omega = _simulate_simple_pendulum_arrays(
        theta0, omega0, g, L, dt, t_max, gamma, A_drive, omega_drive
    )
    return pd.DataFrame(
        {"time": t, "theta_rad": theta, "theta_deg": np.degrees(theta), "omega": omega}
    )


def zero_crossing_times(theta, time):
    crossings = []
    for i in range(1, len(theta)):
        if theta[i - 1] * theta[i] < 0:
            t_cross = time[i - 1] - theta[i - 1] * (time[i] - time[i - 1]) / (
                theta[i] - theta[i - 1]
            )
            crossings.append(t_cross)
    return crossings


if __name__ == "__main__":
    n_angles = 10
    colors = plt.cm.viridis(np.linspace(0.1, 0.9, n_angles))

    # ── Figure 1: phase portrait ──────────────────────────────────────────────────
    fig1, ax1 = plt.subplots(figsize=(3.4, 2.8))
    for idx in range(n_angles):
        theta0 = np.radians(15 * idx)
        df = simulate_simple_pendulum(theta0, 0.0)
        ax1.plot(df["theta_rad"], df["omega"],
                 color=colors[idx], label=rf'$\theta_0={15*idx}^\circ$',
                 linewidth=0.9)
    ax1.set_xlabel(r'$\theta$ (rad)')
    ax1.set_ylabel(r'$\dot\theta$ (rad s$^{-1}$)')
    ax1.legend(fontsize=7, ncol=2)
    plt.tight_layout(pad=0.6)

    # ── Figure 2: θ(t) with zero-crossing markers ─────────────────────────────────
    n_angles2 = 20
    colors2 = plt.cm.viridis(np.linspace(0.1, 0.9, n_angles2))
    fig2, ax2 = plt.subplots(figsize=(3.4, 2.8))
    for idx, i in enumerate(range(-10, 10)):
        theta0 = np.radians(10 * i)
        df = simulate_simple_pendulum(theta0, 0.0)
        ax2.plot(df["time"], df["theta_rad"],
                 color=colors2[idx], linewidth=0.9)
        crossings = zero_crossing_times(df["theta_rad"], df["time"])
        if crossings:
            ax2.scatter(crossings, [0] * len(crossings),
                        color=colors2[idx], s=6, zorder=3, linewidths=0)
    ax2.set_xlabel(r'$t$ (s)')
    ax2.set_ylabel(r'$\theta$ (rad)')
    plt.tight_layout(pad=0.6)

    plt.show()
