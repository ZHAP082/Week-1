#Importing
import numpy as np
import matplotlib.pyplot as plt
#Making each thing in the file into separate lists where each elemnt is float.
f = open('Galaxy1 (4).txt','r')
list_make = f.readlines()

All_data = []
Radias  = []
velocity = []
change_in_radias = []
change_in_velocity = []
Mass = []

for line in list_make:
    make_each_list = line.split('\t')
    All_data.append(make_each_list)

for i in All_data:
    Radias.append(i[0])
    velocity.append(i[1])
    change_in_radias.append(i[2])
    change_in_velocity.append(i[3])
    Mass.append(i[4])
    
Radias_Q = (Radias[1:])
velocity_Q = (velocity[1:])
change_in_radias_Q = (change_in_radias[1:])
change_in_velocity_Q = (change_in_velocity[1:])
Mass_data_n_Q = (Mass[1:])

Mass_data_Q = []

for i in Mass_data_n_Q:
    Just_data = i.replace('\n','')
    Mass_data_Q.append(Just_data)

Radias_data = []
velocity_data = []
change_in_radias_data = []
change_in_velocity_data = []
Mass_data = []

for i in Radias_Q:
    Radias_data.append(float(i))

for i in velocity_Q:
    velocity_data.append(float(i))

for i in change_in_radias_Q:
    change_in_radias_data.append(float(i))

for i in change_in_velocity_Q:
    change_in_velocity_data.append(float(i))

for i in Mass_data_Q:
    Mass_data.append(float(i))

# Making arrays for all titles

Radias_data_array = np.array(Radias_data)
velocity_data_array = np.array(velocity_data)
change_in_radias_data_array = np.array(change_in_radias_data)
change_in_velocity_data_array = np.array(change_in_velocity_data)
Mass_data_array = np.array(Mass_data)

# Q.6 Ploting Graph v(r) = velocity (y) as a function of radias (x)

plt.plot(Radias_data_array,velocity_data_array)

plt.xlabel ('Radias / kpc')
plt.ylabel ('velocity / km/s')
plt.title ('Velocity as a function of radias')
plt.show()




