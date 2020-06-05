import numpy as np
import matplotlib.pyplot as plt


f = open('Galaxy1 (4).txt')
f.readline()

radias = []

for line in f:
  radias.append(float(line.split('\t')[0]))

x = np.array(radias)

print (x)