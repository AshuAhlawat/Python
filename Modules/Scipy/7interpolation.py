import numpy as np
import scipy.interpolate as sp


xs = np.arange(10)
print(xs)
ys = 3*xs + 1
print(ys)

interp_func = sp.interp1d(xs,ys)
print(interp_func)

xm = np.arange(3.1, 5, 0.1)
print(xm)

newarr = interp_func(np.arange(3.1, 5, 0.1))
print(newarr)

# ys = xs**2 + np.sin(xs) + 1

# interp_func = sp.UnivariateSpline(xs, ys)
# interp_func = sp.Rbf(xs, ys)

# newarr = interp_func(np.arange(2.1, 3, 0.1))