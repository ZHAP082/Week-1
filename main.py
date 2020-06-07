f = open('Galaxy1 (4).txt','r')#open file in read mode
list_make = f.readlines()#reads file and makes it into a list

All_data = []#makes empty list Main
Radias  = []#makes empty list Radias

for line in list_make:#iterates through the file which we made a list
    make_each_list = line.split('\t')#split the list making each line its own list
    All_data.append(make_each_list)#adds to the list All_data each line. This makes it a list with multiple lists each a line



for i in All_data:#iterates through All_data
    Radias.append(i[0])#Adds the element 0 from each line aka the radias from All_data data
    

Radias_data = (Radias[1:])#Radias list along with the radias data includes the title. We only want data so we use slicing to get rid of first elemnent which is the title.
