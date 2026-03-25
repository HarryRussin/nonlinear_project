from rk4 import RK4
import numpy as np
import matplotlib.pyplot as plt
import plot_style  # noqa: F401 — sets rcParams

dt = 0.1 #s
t = 0 #s
m = 1 #kg
k = 1 #N/m

period = 2*np.pi*np.sqrt(m/k)
T_10 = 10*period
steps = int(T_10/dt)
times = np.linspace(0, T_10, steps, endpoint=False)
positions = np.zeros(steps)
velocities = np.zeros(steps)

def ODE(t,y):
    #set initial conditions for x and v
    x = y[0]
    v = y[1]        
    dxdt = v
    dvdt = -k*x/m
    #a = f/m
    return np.asarray([dxdt, dvdt])

y = np.asarray([1,0])

for i, t in enumerate(times):
    y = RK4(t, y, ODE, dt)
    positions[i] = y[0]
    velocities[i] = y[1]

def analytical_solution(t):
    A = 1
    w = np.sqrt(k/m)
    # x(t) = Acos(wt + phi)
    return A*np.cos(w*t)

a_positions = np.zeros(steps)

for i, t in enumerate(times):
    a_positions[i] = analytical_solution(t)

def potential_energy(x):
    return 0.5*k*x**2

def kinetic_energy(v):
    return 0.5*m*v**2


energies = np.zeros(steps)
init_e = potential_energy(positions[0]) + kinetic_energy(velocities[0])

for i in range(steps):
    #record the ratio of energy to intiial energy
    if potential_energy(positions[i]) != 0:
        energies[i] = (kinetic_energy(velocities[i]) + potential_energy(positions[i]))/init_e
    else:
        energies[i] = kinetic_energy(velocities[i])/init_e




#for importing and good code practice 😎
if __name__ == "__main__":
    error = np.abs(positions - a_positions)

    fig, axes = plt.subplots(3, 1, figsize=(3.4, 7.0), sharex=True)

    # Panel (a): position — RK4 vs analytic
    axes[0].plot(times, a_positions, '--', color='0.55',
                 label=r'$x(t)$ analytic', linewidth=0.9)
    axes[0].plot(times, positions, 'k-',
                 label=r'$x(t)$ RK4', linewidth=0.9)
    axes[0].fill_between(times, positions - error, positions + error,
                         color='0.4', alpha=0.25, linewidth=0)
    axes[0].set_ylabel(r'$x$ (m)')
    axes[0].legend()

    # Panel (b): velocity
    axes[1].plot(times, velocities, 'k-', linewidth=0.9)
    axes[1].set_ylabel(r'$\dot x$ (m s$^{-1}$)')

    # Panel (c): energy conservation ratio
    axes[2].plot(times, energies, 'k-', linewidth=0.9)
    axes[2].axhline(1.0, color='0.6', linewidth=0.7, linestyle='--')
    axes[2].set_ylabel(r'$E(t)/E_0$')
    axes[2].set_xlabel(r'$t$ (s)')

    plt.tight_layout(pad=0.6)
    plt.show()

#FUNCTION EVERYTHING IN A FUNCTION YIP

def mass_spring_system(m, k, dt, T_10, x0, v0):
    steps = int(T_10/dt)
    times = np.linspace(0, T_10, steps, endpoint=False)
    positions = np.zeros(steps)
    velocities = np.zeros(steps)
    def ODE(t,y):
        #set initial conditions for x and v
        x = y[0]
        v = y[1]        
        dxdt = v
        dvdt = -k*x/m
        #a = f/m
        return np.asarray([dxdt, dvdt])
    
    y = np.asarray([x0,v0])
    for i, t in enumerate(times):
        y = RK4(t, y, ODE, dt)
        positions[i] = y[0]
        velocities[i] = y[1]

    def analytical_solution(t):
        A = x0
        w = np.sqrt(k/m)
        # x(t) = Acos(wt + phi)
        return A*np.cos(w*t)
    
    a_positions = np.zeros(steps)
    for i, t in enumerate(times):
        a_positions[i] = analytical_solution(t)
        
    def potential_energy(x):
        return 0.5*k*x**2
    def kinetic_energy(v):
        return 0.5*m*v**2
    
    error = np.abs(positions - a_positions)
    
    energies = np.zeros(steps)
    init_e = potential_energy(positions[0]) + kinetic_energy(velocities[0])
    for i in range(steps):
        #record the ratio of energy to intiial energy
        if potential_energy(positions[i]) != 0:
            energies[i] = (kinetic_energy(velocities[i]) + potential_energy(positions[i]))/init_e
        else:
            energies[i] = kinetic_energy(velocities[i])/init_e

    return times, positions, velocities, energies, error
