import matplotlib.pyplot as plt
import seaborn
import numpy.random as rdm

x = rdm.binomial(n=10, p=0.9, size=20)

print(x)

seaborn.displot(x)
plt.show()

print(x)
