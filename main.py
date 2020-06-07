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
    
Radias_data = (Radias[1:])
velocity_data = (velocity[1:])
change_in_radias_data = (change_in_radias[1:])
change_in_velocity_data = (change_in_velocity[1:])
Mass_data_n = (Mass[1:])

Mass_data = []
for i in Mass_data_n:
    Just_data = i.replace('\n','')
    Mass_data.append(Just_data)

#Making arrays for each thing


