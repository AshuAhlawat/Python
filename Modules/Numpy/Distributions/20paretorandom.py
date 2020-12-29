from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.pareto(scale=2, size=(2, 3))

print(x)

sns.displot(x,hist=False,label="pareto")

plt.show()