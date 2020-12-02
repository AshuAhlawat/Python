#a library that converts into Arrays 
import numpy

arrp=[[1,2,3,4,5], [6,7,8,9,10]]
arr = numpy.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -1])
print(arrp[1][-1])

print(arr[0:2, 1:4])
