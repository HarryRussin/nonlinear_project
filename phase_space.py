from mass_spring import mass_spring_system
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plot_style  # noqa: F401 — sets rcParams

initial_conditions = np.arange(0, 1.1, 0.1)
data = []
for v0 in initial_conditions:
    times, positions, velocities, energies, error = mass_spring_system(
        1, 1, 0.1, 10 * 2 * np.pi * np.sqrt(1 / 1), 1, v0
    )
    data.append({'v0': v0, 'positions': positions, 'velocities': velocities})
df = pd.DataFrame(data)

colors = plt.cm.viridis(np.linspace(0.1, 0.9, len(initial_conditions)))

fig, ax = plt.subplots(figsize=(3.4, 2.8))
for i, v0 in enumerate(initial_conditions):
    ax.plot(df['positions'][i], df['velocities'][i],
            color=colors[i], label=rf'$v_0={v0:.1f}$', linewidth=0.9)
ax.set_xlabel(r'$x$ (m)')
ax.set_ylabel(r'$\dot x$ (m s$^{-1}$)')
ax.legend(fontsize=7, loc='upper left', bbox_to_anchor=(1, 1))
plt.tight_layout(pad=0.6)
plt.show()
