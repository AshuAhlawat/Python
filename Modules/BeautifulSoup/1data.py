import requests

def offlinesite(x):
    
    r1 = requests.get(x)
    r2 = requests.get("https://cdn.myanimelist.net/images/userimages/6476477.jpg")
    
    if r1.ok and r2.ok:
        
        print("\n\nStatus : \n  OK\n\n\nSite Information :\n",r1.headers)
        
        try:
            f1 = open("C:/Users/ashua/OneDrive/Desktop/Coding/Python/Modules/BeautifulSoup/1data.html","w+",encoding="utf-8")
            f1.write(r1.text)
            f2 = open("C:/Users/ashua/OneDrive/Desktop/Coding/Python/Modules/BeautifulSoup/1img.jpg","wb")
            f2.write(r2.content)
        except:
            print("Error Occured")
        finally:
            f1.close()
            f2.close()


def main():
    
    site = str(input("Enter URL : "))
    #http://mynovellist.herokuapp.com/home/
    offlinesite(site)
    
main()