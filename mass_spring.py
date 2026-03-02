from rk4 import RK4
import numpy as np
import matplotlib.pyplot as plt

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
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 15))
    plt.subplots_adjust(hspace=0.5)
    ax1.plot(times, velocities, label='Velocity')
    ax1.errorbar(times,positions, yerr=error, alpha=0.8, label='Position with error bars')
    ax1.set_title('Mass-Spring System')
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Velocity (m/s) and Position (m)')
    ax1.grid()
    ax1.legend()
    ax2.set_ylim(0.9, 1.1)
    ax2.plot(times, energies, label='E(t)/E0')
    ax2.set_title('Energy of Mass-Spring System')
    ax2.set_xlabel('Time (s)')
    ax2.set_ylabel('Energy (J)')
    ax2.grid()
    ax2.legend()
    ax3.plot(times, energies, label='zoomed energy')
    ax3.set_xlabel('Time (s)')
    ax3.set_ylabel('Energy (J)')
    ax3.grid()
    ax3.legend()
    plt.grid()
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
