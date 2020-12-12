from numpy import random
import seaborn
import matplotlib.pyplot as plt

x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
print(x)
seaborn.displot(x,hist=False,label="multinomial")
plt.show()
