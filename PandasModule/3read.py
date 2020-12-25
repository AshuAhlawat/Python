import pandas as pd

c = pd.read_csv("Python\PandasModule\datac1.csv")
print(c)

df = pd.read_json('Python\PandasModule\dataj.json')
print(df.to_string()) 