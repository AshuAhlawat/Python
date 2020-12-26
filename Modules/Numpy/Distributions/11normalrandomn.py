import seaborn
import matplotlib.pyplot as mpl
import numpy

arr=numpy.random.normal(loc=1, scale=8, size=(2, 3))

print(arr)
seaborn.distplot(arr)

mpl.show()
