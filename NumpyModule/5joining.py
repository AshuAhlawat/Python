import numpy

print("\n\n__________________________________\n")
arr1 = numpy.array([1, 2, 3])
arr2 = numpy.array([4, 5, 6])

arr = numpy.concatenate((arr1, arr2))
print(arr,"\n")

arr = numpy.stack((arr1, arr2))
print(arr,"\n")
arr = numpy.stack((arr1, arr2),axis=1)
print(arr,"\n__________________________________\n")

arr1 = numpy.array([[1, 2], [3, 4]])
arr2 = numpy.array([[5, 6], [7, 8]])

arr = numpy.concatenate((arr1, arr2))
print(arr,"\n")
arr = numpy.concatenate((arr1, arr2),axis=1)
print(arr,"\n")

arr = numpy.stack((arr1, arr2))
print(arr,"\n")
arr = numpy.stack((arr1, arr2),axis=1)
print(arr,"\n__________________________________\n")

arr1 = numpy.array([1, 2, 3])
arr2 = numpy.array([4, 5, 6])

arr = numpy.hstack((arr1, arr2))
print(arr,"\n")

arr = numpy.vstack((arr1, arr2))
print(arr,"\n")

arr = numpy.dstack((arr1, arr2))
print(arr,"\n__________________________________\n")


arr1 = numpy.array([[1, 2], [3, 4]])
arr2 = numpy.array([[5, 6], [7, 8]])

arr = numpy.hstack((arr1, arr2))
print(arr,"\n")

arr = numpy.vstack((arr1, arr2))
print(arr,"\n")

arr = numpy.dstack((arr1, arr2))
print(arr,"\n__________________________________\n")