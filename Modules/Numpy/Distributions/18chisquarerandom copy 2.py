from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.chisquare(scale=2, size=(2, 3))

print(x)

sns.displot(x,hist=False,label="chisquare")

plt.show()