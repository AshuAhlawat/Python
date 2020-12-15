import seaborn
import matplotlib.pyplot as mpl
import numpy

arr=numpy.random.normal(loc=1, scale=2, size=(2, 3))

print(arr)
seaborn.distplot(arr)

mpl.show()
