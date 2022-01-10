import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford", "Tata"],
  'passings': [3, 7, 2, 5]
}
myvar = pd.DataFrame(mydataset,index = ["car1","car2","car3","car4"])

print(myvar)
print(myvar.loc["car2"])

mydataset = ["BMW", ["Volvo", "Ford"], "Tata"]

myvar = pd.DataFrame(mydataset)
print(myvar)

#df = pd.read_csv('data.csv')
