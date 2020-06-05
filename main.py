import numpy as np
import matplotlib.pyplot as plt
x = np.array([1,2,3,4,5,6])
y = np.array([10,100,1000,10000,100000,1000000])
y = np.log10(y)
plt.plot(x,y,'ro')
plt.xlabel('Pressure/Pa')
plt.ylabel('Volume/m$ˆ3$')
plt.axis([0,7,0,7])
plt.show()

