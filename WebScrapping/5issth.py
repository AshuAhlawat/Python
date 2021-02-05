from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:\ProgramData\chromedriver.exe")
driver.get("https://www.novels.pl/novel/I-Shall-Seal-the-Heavens/201/Chapter-201-The-Dao-Child-Fights.html")

import time

def downloadloop(x):
    try:
        match = WebDriverWait(driver,3).until(
            EC.presence_of_element_located(
            (By.ID,'aswift_7')
            )
        )
        iframe = driver.find_element_by_id('aswift_7')
        driver.switch_to.frame(iframe)
        search_a = driver.find_element_by_id("dismiss-button")
        search_a.click()
    except Exception as e:
        print(e)
    finally:
        driver.switch_to.default_content()
    driver.switch_to.default_content()
    match = WebDriverWait(driver,10).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME,'_download')
        )
    )

    search_d = driver.find_element_by_class_name("_download")
    search_d.click()
    time.sleep(3)
    search_n = driver.find_elements_by_css_selector('a[href^="/novel/"]')
    search_n[1].click()
    time.sleep(3)
    print("\n\nChapter "+str(x)+" downloaded")
    x = x+1
    downloadloop(x)

downloadloop(201)