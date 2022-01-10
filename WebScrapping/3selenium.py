from selenium import webdriver

driver = webdriver.Chrome("C:\ProgramData\chromedriver.exe")

driver.get("http://mynovellist.herokuapp.com/home/")
print('\n\n',driver.title)
driver.close()