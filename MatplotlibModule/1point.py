import matplotlib.pyplot as plt
import numpy as np

point1 = np.array([1,4])
point2 = np.array([4,1])
point3 = np.array([2,2])
point4 = np.array([2,2])

plt.plot(point1,point2,'o')
plt.plot(point3,point4,'o')

plt.show()