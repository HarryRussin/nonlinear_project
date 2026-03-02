from mass_spring import mass_spring_system
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#why is it opening a graaph when i run it? I just want to run the code and get the dataframe, not show the graph


initial_conditions = np.arange(0, 1.1, 0.1)
data = []
for v0 in initial_conditions:
    times, positions, velocities, energies, error = mass_spring_system(1, 1,0.1, 10*2*np.pi*np.sqrt(1/1), 1, v0) 
    data.append({'v0': v0, 'positions': positions, 'velocities': velocities})
df = pd.DataFrame(data)

    
for i, v0 in enumerate(initial_conditions):
    plt.plot(df['positions'][i], df['velocities'][i], label=f'v0={v0}')
plt.xlabel('Position (m)')
plt.ylabel('Velocity (m/s)')    
plt.title('Phase Space of Mass-Spring System')
plt.grid()
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.show()
