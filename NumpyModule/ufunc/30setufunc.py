import numpy as np

arr = np.array([0.1, 0.2, 0.5])

x = np.arctanh(arr)
print(x)

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

newarr = np.union1d(arr1, arr2)
print(newarr)

newarr = np.intersect1d(arr1, arr2)
print(newarr)

newarr = np.setdiff1d(arr1, arr2)
print(newarr)

newarr = np.setdiff1d(arr2, arr1)
print(newarr)

newarr = np.setxor1d(arr1, arr2)
print(newarr)