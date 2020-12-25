import pandas as pd
import matplotlib.pyplot as plt

x = pd.read_csv("Python\PandasModule\datac1.csv")

x.plot(kind = 'scatter', x='Duration', y='Maxpulse')
x["Duration"].plot(kind = 'hist')
x.plot()

plt.show()