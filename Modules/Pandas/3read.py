import pandas as pd

c = pd.read_csv("Python\Modules\Pandas\datac1.csv")
print(c)

df = pd.read_json('Python\Modules\Pandas\dataj.json')
print(df.to_string())