import numpy as np

arr = np.array([3, 6, 9])
x = np.lcm.reduce(arr)
print(x)

x = np.lcm.reduce(np.arange(1, 11))
print(x)

x = np.gcd.reduce(arr)
print(x)