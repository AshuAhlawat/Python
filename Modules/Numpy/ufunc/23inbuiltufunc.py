import numpy as numpy

arr1 = numpy.array([10, 11, 12, 13, 14, 15])
arr2 = numpy.array([20, 21, 22, 23, 24, 25])
arr3 = numpy.array([1,2,3,2,2,1])
newarr = numpy.add(arr1, arr2)
print(newarr)

newarr = numpy.subtract(arr1, arr2)
print(newarr)

newarr = numpy.multiply(arr1, arr2)
print(newarr)

newarr = numpy.divide(arr1, arr2)
print(newarr)

newarr = numpy.power(arr1, arr3)
print(newarr)

newarr = numpy.mod(arr1, arr2)
print(newarr)

newarr = numpy.remainder(arr1, arr2)
print(newarr)

newarr = numpy.divmod(arr1, arr2)
print(newarr)