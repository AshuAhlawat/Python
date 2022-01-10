import numpy as np

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

arr[0] = 42

print(x)
print(y)

arr[0] = 9

x = arr.copy()

print(x)
print(y)