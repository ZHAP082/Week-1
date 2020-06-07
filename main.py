f = open('Galaxy1 (4).txt','r')#open file in read mode
list_make = f.readlines()#reads file and makes it into a list

All_data = []#makes empty list Main
Radias  = []#makes empty list Radias
velocity = []
change_in_radias = []
change_in_velocity = []
Mass = []

for line in list_make:#iterates through the file which we made a list
    make_each_list = line.split('\t')#split the list making each line its own list
    All_data.append(make_each_list)#adds to the list All_data each line. This makes it a list with multiple lists each a line

for i in All_data:#iterates through All_data
    Radias.append(i[0])#Adds the element 0 from each line aka the radias from All_data data
    velocity.append(i[1])
    change_in_radias.append(i[2])
    change_in_velocity.append(i[3])
    Mass.append(i[4])
    
Radias_Q = (Radias[1:])#Radias list along with the radias data includes the title. We only want data so we use slicing to get rid of first elemnent which is the title.
velocity_Q = (velocity[1:])
change_in_radias_Q = (change_in_radias[1:])
change_in_velocity_Q = (change_in_velocity[1:])
Mass_data_n_Q = (Mass[1:])#Mass data has a thing where all the stuff element have a \n at the end.

#Getting rid of the \n

Mass_data_Q = []

for i in Mass_data_n_Q:
    Just_data = i.replace('\n','')#Getting rid /n
    Mass_data_Q.append(Just_data)

#One last thing to fix. Right now inside all the things (Radias, velocity, ...)
#All the data are strings so we need to make them into floats.    

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


