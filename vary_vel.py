from simple_pendulum import simulate_simple_pendulum
import matplotlib.pyplot as plt
import numpy as np
import plot_style  # noqa: F401 — sets rcParams

# ── Figure 1: θ(t) for varying initial angular velocity ──────────────────────
indices1 = [i for i in range(-5, 5) if i != 0]
colors1  = plt.cm.viridis(np.linspace(0.1, 0.9, len(indices1)))

fig1, ax1 = plt.subplots(figsize=(3.4, 2.8))
for col, i in zip(colors1, indices1):
    df = simulate_simple_pendulum(np.radians(45), np.radians(50 * i))
    ax1.plot(df['theta_rad'], df['time'], '.', markersize=0.6,
             color=col, label=rf'$\dot\theta_0={50*i}^\circ$')
ax1.set_xlabel(r'$\theta$ (rad)')
ax1.set_ylabel(r'$t$ (s)')
ax1.legend(fontsize=6, ncol=2)
plt.tight_layout(pad=0.6)

# ── Figure 2: phase portrait for varying initial conditions ───────────────────
indices2 = list(range(-10, 10))
colors2  = plt.cm.viridis(np.linspace(0.1, 0.9, len(indices2)))

fig2, ax2 = plt.subplots(figsize=(3.4, 2.8))
for col, i in zip(colors2, indices2):
    df = simulate_simple_pendulum(np.radians(100), np.radians(100 * i))
    ax2.scatter(df['theta_rad'], df['omega'],
                s=0.2, color=col, linewidths=0, rasterized=True)
ax2.set_xlabel(r'$\theta$ (rad)')
ax2.set_ylabel(r'$\dot\theta$ (rad s$^{-1}$)')
plt.tight_layout(pad=0.6)

plt.show()