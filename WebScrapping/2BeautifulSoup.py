import requests

r = requests.get("https://en.wikipedia.org/wiki/Economy_of_India")
with open("./economy.html","w",encoding="utf-8") as f:
    f.write(r.text)

from bs4 import BeautifulSoup

with open("./economy.html",encoding="utf-8") as f:
    soup = BeautifulSoup(f ,'html5lib')

match_gdp_table = soup.find('table',class_="wikitable")

# print(match_gdp_table)

match_gdp_entries = match_gdp_table.find_all('tr')
# print(match_gdp_entries[0])

gdp_entries_list_=[]
for match in match_gdp_entries:
    gdp_entries_list_.append(match.text)

# print(gdp_entries_list_)

gdp_entries_list=[]
for entry in gdp_entries_list_:
    x = entry.split("\n\n")
    gdp_entries_list.append(x)

# print(gdp_entries_list)
with open("./economy.csv","w") as f:
    f.write("")

with open("./economy.csv","a") as f:
    # gdp_entries_list[0][3]=gdp_entries_list[0][3].replace("\xa0","")
    # gdp_entries_list[0][6]=gdp_entries_list[0][6].replace("\xa0","")
    for i in range(len(gdp_entries_list)):
        row = gdp_entries_list[i]

        for j in range(len(row)):
            el = row[j]
            el = el.replace(",","")
            el = el.replace("%","")                
            el = el.replace("\n","")
            el = el.replace("n/a","")

            gdp_entries_list[i][j] = el

        f.write(",".join(gdp_entries_list[i])+"\n")
                # f.write(el)
                # f.write(',')
# print(gdp_entries_list)

import pandas as pd
import matplotlib.pyplot as plt

gdp=pd.read_csv("./economy.csv")
# print(gdp.columns)

gdp = gdp.dropna()

# print(gdp.info())

year=gdp["Year"]
gdpinbill=gdp["GDP(Bil. US$PPP)"]
# gdpcapita=gdp["GDP per capita(in US$ PPP)"]
# gdpgrowth=gdp["GDP growth(real)"]
# gdpinflation=gdp["Inflation rate(in Percent)"]
# gdpshare=gdp["Share of world(GDP PPP in)"]
# gdpdebt=gdp["Government debt( of GDP)"]

fig, ax = plt.subplots(2, 3, figsize=(18,8))


ax[0,0].plot(year,gdpinbill,c="cyan",alpha=0.5,ls=":",lw=2,marker="o")
plt.xlabel("Year")
plt.ylabel("Bill$")
plt.title("Year/GDP in BILL")

# plt.subplot(3,2,2)
# plt.plot(year,gdpcapita,c="green",ls="--",lw=0.7,marker="*")
# plt.xlabel("Year")
# plt.ylabel("Gdp Capita")
# plt.title("Year/Gdp in capita")

# plt.subplot(3,2,3)
# plt.plot(year,gdpgrowth,c="blue",ls="-.",lw=0.7,marker="4")
# plt.xlabel("Year")
# plt.ylabel("Gdp Growth")
# plt.title("Year/GDP Growth(%)")

# plt.subplot(3,2,4)
# plt.plot(year,gdpinflation,c="brown",ls="-",lw=0.7,marker="*")
# plt.xlabel("Year")
# plt.ylabel("Inflation")
# plt.title("Year/Inflation(%)")

# plt.subplot(3,2,5)
# plt.plot(year,gdpshare,c="red",ls="-",lw=0.7,marker="o")
# plt.xlabel("Year")
# plt.ylabel("GDP Share(%)")
# plt.title("Year/Global Share")

# plt.subplot(3,2,6)
# plt.plot(year,gdpdebt,c="black",ls=":",lw=0.9,marker="4")
# plt.xlabel("Year")
# plt.ylabel("Debt(%)")
# plt.title("Year/GDP Debt")

# plt.suptitle("Economy Chart of India")   

plt.show()


