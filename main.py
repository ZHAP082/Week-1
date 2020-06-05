import numpy as np
import matplotlib.pyplot as plt
datapoints = 100
x = np.arange(datapoints)
y = np.sin(2 * np.pi * x/datapoints)
plt.plot(x,y)
plt.xlabel('datapoints')
plt.ylabel('sin(2$\pi$ datapoints)')
plt.show()
