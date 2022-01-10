# id -> name -> class -> actual HTML
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\ProgramData\chromedriver.exe")
driver.get("http://mynovellist.herokuapp.com/register/login/")
print(driver.title)


match_username = driver.find_element_by_id("id_username")
match_username.send_keys("Capti")
match_password = driver.find_element_by_id("id_password")
match_password.send_keys("SandyRuby@12")
match_password.send_keys(Keys.ENTER)

try:
    match_completed = WebDriverWait(driver,20).until(
        expected_conditions.presence_of_element_located(
            (By.ID, "completed")
        )
    )
    
    complete_list = match_completed.find_elements_by_tag_name("td")
    print("")
    for _ in complete_list:
        print(_.get_attribute('innerHTML'))
    
except :
    print("Error : ", Exception)
finally :
    driver.quit()

