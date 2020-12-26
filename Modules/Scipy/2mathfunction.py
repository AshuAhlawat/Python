import scipy.optimize as sp
import math

def eqn(x):
    return math.sin(x)+math.cos(x)

myroot = sp.root(eqn, 1)
mymaxima = sp.minimize(eqn, 0, method = 'BFGS')

print(myroot.x, mymaxima.x)