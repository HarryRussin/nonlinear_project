"""
Shared matplotlib style for publication-quality figures.
Import this module (side-effect only) at the top of any plotting script:

    import plot_style  # noqa: F401
"""
import matplotlib as mpl

mpl.rcParams.update({
    # Font
    'font.family':        'serif',
    'font.size':          9,
    'axes.labelsize':     9,
    'axes.titlesize':     9,
    'xtick.labelsize':    8,
    'ytick.labelsize':    8,
    'legend.fontsize':    8,
    # Axes
    'axes.linewidth':     0.8,
    'axes.spines.top':    True,
    'axes.spines.right':  True,
    # Ticks — inward on all four sides (physics convention)
    'xtick.major.width':  0.8,
    'ytick.major.width':  0.8,
    'xtick.minor.width':  0.6,
    'ytick.minor.width':  0.6,
    'xtick.major.size':   3.5,
    'ytick.major.size':   3.5,
    'xtick.direction':    'in',
    'ytick.direction':    'in',
    'xtick.top':          True,
    'ytick.right':        True,
    # Lines
    'lines.linewidth':    1.0,
    # Legend
    'legend.frameon':     False,
    'legend.handlelength': 1.5,
    # Output
    'figure.dpi':         150,
    'savefig.dpi':        300,
    'savefig.bbox':       'tight',
})
