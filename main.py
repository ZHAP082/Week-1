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
plt.title ('Velocity (Blue) and Predicted (Orange) Velocity as a function of radias')
#plt.show() Since we want to plot 2 lines on same graph with theses axis tis plt.show() needed to be after the other plot is made.

#Q.7 - Finding predicted velocity from each radias and making into array (done automatically since we used previous arrays to make it.-  
# v_predicted = sqr((G*Mc) / r)
#For Mc and r are in Galaxy.txt
#G = 4.30×10^−6 kpc/M⊙ (km/s)2 for the scales I am using.

velocity_predicted_array = np.sqrt(((4.30*10**-6)*Mass_data_array)/Radias_data_array)

#Q.8 - Plotting pv(r) (pv = y and r = x) on the same axes as v(x)

plt.plot(Radias_data_array,velocity_predicted_array)
plt.show()
#No need for diffrent labels since same as previous plot. I changed title so it inclues both v and predicted v.








