import matplotlib.pyplot as plt
import numpy as np

line1x = np.array([2,4,4,2,2])
line1y = np.array([2,2,4,4,2])

line2x = np.array([2.5,3.5,3.5,2.5,2.5])
line2y = np.array([2.5,2.5,3.5,3.5,2.5])

plt.plot(line1x,line1y,marker= '*',ls='dotted',c='g',linewidth='3')
plt.plot(line2x,line2y,c='r',marker='o', ls='-.',lw='1' )

plt.show()