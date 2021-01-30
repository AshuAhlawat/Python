
def run():
    import requests

    r = requests.get("https://en.wikipedia.org/wiki/Economy_of_India")
    with open("C:\ProgramData\GdpPlot\cache\economy.html","w",encoding="utf-8") as f:
        f.write(r.text)

    from bs4 import BeautifulSoup

    with open("C:\ProgramData\GdpPlot\cache\economy.html",encoding="utf-8") as f:
        soup = BeautifulSoup(f ,'html5lib')

    match_gdp_table = soup.find('table',class_="wikitable sortable")

    match_gdp_entries = match_gdp_table.find_all('tr')

    gdp_entries_list_=[]
    for match in match_gdp_entries:
        gdp_entries_list_.append(match.text)

    gdp_entries_list=[]
    for entry in gdp_entries_list_:
        x = entry.split("\n\n")
        gdp_entries_list.append(x)

    # for entry in gdp_entries_list:
    #     print(entry)

    with open("C:\ProgramData\GdpPlot\cache\economy.csv","w") as f:
        gdp_entries_list[0][3]=gdp_entries_list[0][3].replace("\xa0","")
        gdp_entries_list[0][6]=gdp_entries_list[0][6].replace("\xa0","")
        for entry in gdp_entries_list:
            
            for _ in entry:
                    
                if _ == entry[0]:
                    x = _.split('\n')
                    f.write(x[1])
                    f.write(",")
                
                elif _ == entry[6]:
                    y=_.split('\n')
                    if "%" in y[0]:
                        y[0] = y[0].replace("%","")
                    f.write(y[0])
                    f.write('\n')
                else:
                    if "%" in _:
                        _ = _.replace("%","")
                    
                    if "," in _:
                        _ = _.replace(",","")
                    
                    f.write(_)
                    f.write(',')
                    
    import pandas as pd
    import matplotlib.pyplot as plt

    with open("C:\ProgramData\GdpPlot\cache\economy.csv") as f:
        gdp_list=pd.read_csv(f)

        year=gdp_list["Year"]
        gdpinbill=gdp_list["GDP(in bil. US$ PPP)"]
        gdpcapita=gdp_list["GDP per capita(in US$ PPP)"]
        gdpgrowth=gdp_list["GDP growth(real)"]
        gdpinflation=gdp_list["Inflation rate(in Percent)"]
        gdpshare=gdp_list["Share of world(GDP PPP in)"]
        gdpdebt=gdp_list["Government debt(in of GDP)"]

    
    plt.subplot(3,2,1)
    plt.plot(year,gdpinbill,c="cyan",alpha=0.5,ls=":",lw=0.7,marker="o")
    plt.xlabel("Year")
    plt.ylabel("Bill$")
    plt.title("Year/GDP in BILL")

    plt.subplot(3,2,2)
    plt.plot(year,gdpcapita,c="green",ls="--",lw=0.7,marker="*")
    plt.xlabel("Year")
    plt.ylabel("Gdp Capita")
    plt.title("Year/Gdp in capita")

    plt.subplot(3,2,3)
    plt.plot(year,gdpgrowth,c="blue",ls="-.",lw=0.7,marker="4")
    plt.xlabel("Year")
    plt.ylabel("Gdp Growth")
    plt.title("Year/GDP Growth(%)")

    plt.subplot(3,2,4)
    plt.plot(year,gdpinflation,c="brown",ls="-",lw=0.7,marker="*")
    plt.xlabel("Year")
    plt.ylabel("Inflation")
    plt.title("Year/Inflation(%)")

    plt.subplot(3,2,5)
    plt.plot(year,gdpshare,c="red",ls="-",lw=0.7,marker="o")
    plt.xlabel("Year")
    plt.ylabel("GDP Share(%)")
    plt.title("Year/Global Share")

    plt.subplot(3,2,6)
    plt.plot(year,gdpdebt,c="black",ls=":",lw=0.9,marker="4")
    plt.xlabel("Year")
    plt.ylabel("Debt(%)")
    plt.title("Year/GDP Debt")

    plt.suptitle("Economy Chart of India")   

    plt.show()

run()
