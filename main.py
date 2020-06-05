import numpy as np
import matplotlib.pyplot as plt
datapoints = 100
x = np.arange(datapoints)
y = x**3 - (100*x**2) + x + 1
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
