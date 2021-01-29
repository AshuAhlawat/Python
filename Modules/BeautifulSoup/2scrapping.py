import requests

r = requests.get("https://en.wikipedia.org/wiki/Economy_of_India")
with open("economy.html","w",encoding="utf-8") as f:
    f.write(r.text)

from bs4 import BeautifulSoup

with open("economy.html",encoding="utf-8") as f:
    soup = BeautifulSoup(f ,'lxml')

match_gdp_table = soup.find('table',class_="wikitable sortable")

match_gdp_entries = match_gdp_table.find_all('tr')

gdp_entries_list_=[]
for match in match_gdp_entries:
    gdp_entries_list_.append(match.text)

gdp_entries_list=[]
for entry in gdp_entries_list_:
    x = entry.split("\n\n")
    gdp_entries_list.append(x)

for entry in gdp_entries_list:
    print(entry)

with open("economy.csv","w") as f:
    for entry in gdp_entries_list:
        
        for _ in entry:
            if "," in _:
                _ = _.replace(",","")
                
            if "%" in _:
                _ = _.replace("%","")
                
            if _ == entry[0]:
                x = _.split('\n')
                f.write(x[1])
                f.write(",")
            
            elif _ == entry[6]:
                y=_.split('\n')
                f.write(y[0])
                f.write('\n')
            else:
                f.write(_)
                f.write(',')

import pandas as pd

