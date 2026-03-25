from simple_pendulum import simulate_simple_pendulum
import matplotlib.pyplot as plt
import numpy as np
import plot_style  # noqa: F401 — sets rcParams

damping_factors = [0.1, 0.5, 1.0, 2]

dfs = []
for gamma in damping_factors:
    df = simulate_simple_pendulum(np.radians(50), 0.0, gamma=gamma)
    dfs.append(df)

colors = plt.cm.viridis(np.linspace(0.1, 0.9, len(damping_factors)))

# ── Figure 1: time evolution ──────────────────────────────────────────────────
fig1, ax1 = plt.subplots(figsize=(3.4, 2.8))
for i, gamma in enumerate(damping_factors):
    ax1.plot(dfs[i]['time'], dfs[i]['theta_rad'],
             color=colors[i], label=rf'$\gamma={gamma}$', linewidth=0.9)
ax1.set_xlabel(r'$t$ (s)')
ax1.set_ylabel(r'$\theta$ (rad)')
ax1.legend(fontsize=7, ncol=2)
plt.tight_layout(pad=0.6)

# ── Figure 2: phase portraits ─────────────────────────────────────────────────
fig2, ax2 = plt.subplots(figsize=(3.4, 2.8))
for i, gamma in enumerate(damping_factors):
    ax2.plot(dfs[i]['theta_rad'], dfs[i]['omega'],
             color=colors[i], label=rf'$\gamma={gamma}$', linewidth=0.9)
ax2.set_xlabel(r'$\theta$ (rad)')
ax2.set_ylabel(r'$\dot\theta$ (rad s$^{-1}$)')
ax2.legend(fontsize=7, ncol=2)
plt.tight_layout(pad=0.6)

plt.show()
