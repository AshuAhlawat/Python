import numpy as np

arr1 = np.array([90, 60, -30, 360])
x = np.deg2rad(arr1)
#rad2deg()

arr2 = np.array(x)
arr3=np.sin(arr2)

x = np.around(arr3,2)
print(x)


arr = np.array([1, -1, 0.1])

x = np.arcsin(arr)
print(x)

base = 3
perp = 4
x = np.hypot(base, perp)

print(x)