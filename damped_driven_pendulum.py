from simple_pendulum import simulate_simple_pendulum
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# ── Publication style ────────────────────────────────────────────────────────
mpl.rcParams.update({
    'font.family':       'serif',
    'font.size':         9,
    'axes.labelsize':    9,
    'axes.titlesize':    9,
    'xtick.labelsize':   8,
    'ytick.labelsize':   8,
    'legend.fontsize':   8,
    'axes.linewidth':    0.8,
    'xtick.major.width': 0.8,
    'ytick.major.width': 0.8,
    'xtick.direction':   'in',
    'ytick.direction':   'in',
    'xtick.top':         True,
    'ytick.right':       True,
    'figure.dpi':        150,
    'savefig.dpi':       300,
    'lines.linewidth':   1.0,
})

A_drive     = [ 1.47, 1.5]
omega_drive = 0.67
gamma       = 0.5

# Single-column figure width ~ 3.4 in; double-column ~ 7.0 in (APS/IOP standard)
col_w   = 3.4   # inches per panel column
row_h   = 2.6   # inches per row
n       = len(A_drive)
fig, axes = plt.subplots(n, 2,
                         figsize=(col_w * 2, row_h * n),
                         squeeze=False)

for i, A in enumerate(A_drive):
    df = simulate_simple_pendulum(
        0.0, 0.0,
        gamma=gamma, A_drive=A, omega_drive=omega_drive,
        t_max=100000,
    )

    T_drive    = 2 * np.pi / omega_drive
    time_vals  = df['time'].to_numpy()
    n_max      = int(time_vals[-1] / T_drive)
    sample_times = np.arange(50, n_max + 1) * T_drive
    indices    = np.searchsorted(time_vals, sample_times, side='left')
    indices    = np.unique(np.clip(indices, 0, len(time_vals) - 1))

    ax_p = axes[i, 0]   # Poincaré section
    ax_q = axes[i, 1]   # Phase portrait

    # Poincaré section — small black dots, no colour distraction
    ax_p.scatter(
        df['theta_rad'].iloc[indices],
        df['omega'].iloc[indices],
        s=0.8, c='k', linewidths=0, rasterized=True,
    )
    ax_p.set_xlabel(r'$\theta$ (rad)')
    ax_p.set_ylabel(r'$\dot\theta$ (rad s$^{-1}$)')
    ax_p.text(0.97, 0.96, rf'$A={A}$', transform=ax_p.transAxes,
              ha='right', va='top', fontsize=8)
    ax_p.grid(False)

    # Phase portrait — thin grey points; too many to show individually,
    # so use low alpha to suggest density
    ax_q.scatter(
        df['theta_rad'], df['omega'],
        s=0.05, c='k', alpha=0.15, linewidths=0, rasterized=True,
    )
    ax_q.set_xlabel(r'$\theta$ (rad)')
    ax_q.set_ylabel(r'$\dot\theta$ (rad s$^{-1}$)')
    ax_q.grid(False)

# Column headers as panel labels (a), (b) style
axes[0, 0].set_title('Poincaré section')
axes[0, 1].set_title('Phase portrait')

# Row labels on the left margin
for i, A in enumerate(A_drive):
    axes[i, 0].set_ylabel(
        rf'$\dot\theta$ (rad s$^{{-1}}$)',
        labelpad=4,
    )

fig.suptitle(
    rf'Damped driven pendulum: $\gamma={gamma}$, $\omega_d={omega_drive}$ rad s$^{{-1}}$',
    fontsize=9, y=1.01,
)
plt.tight_layout(pad=0.6, h_pad=0.8, w_pad=0.8)
plt.show()

