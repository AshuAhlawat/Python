
button = "green"
poll = "B"

#you id below
id_ = "12016043"
# your password below
pass_ = "SandyRuby@12"

methods = ["Microphone","Listen only"]
method = methods[0]

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.add_argument("start-maximized")
opt.add_experimental_option("prefs", {     "profile.default_content_setting_values.media_stream_mic":1,
})

driver = webdriver.Chrome(options=opt,executable_path="chromedriver.exe")

def onlineclassscript():

    driver.get("https://myclass.lpu.in")

    username = driver.find_element_by_name("i")
    username.send_keys(id_)
    password = driver.find_element_by_name("p")
    password.send_keys(pass_)
    password.send_keys(Keys.ENTER)

    match_search = WebDriverWait(driver,20).until(
        expected_conditions.presence_of_element_located(
            (By.LINK_TEXT, "View Classes/Meetings")
        )
    )

    search = driver.find_element_by_link_text("View Classes/Meetings")
    search.click()

    try:
        match_search = WebDriverWait(driver,20).until(
            expected_conditions.presence_of_element_located(
                (By.CLASS_NAME, "fc-content")
            )
        )
    except:
        quit()
    import time
    while True:
        try:
            time.sleep(1)
            search = driver.find_element_by_css_selector('a[style*="background: '+button+';"]')
            search.click()
            break
        except Exception as e:
            time.sleep(180)
            onlineclassscript()
    
    match_search = WebDriverWait(driver,20).until(
        expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, 'a[role="button"]')
        )
    )
    search = driver.find_element_by_css_selector('a[role="button"]')
    search.click()

    match_search = WebDriverWait(driver,400).until(
        expected_conditions.presence_of_element_located(
            (By.ID, 'frame')
        )
    )
    iframe = driver.find_element_by_id('frame')
    driver.switch_to.frame(iframe)

    match_search = WebDriverWait(driver,20).until(
        expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, 'button[aria-label="' + method +'"]')
        )
    )
    search = driver.find_element_by_css_selector('button[aria-label="' + method +'"]')
    search.click()

    if method=="Microphone":
        match_search = WebDriverWait(driver,20).until(
            expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, 'button[aria-label="Echo is audible"]')
            )
        )
        search = driver.find_element_by_css_selector('button[aria-label="Echo is audible"]')
        search.click()

    while True:
        try:
            match_search = WebDriverWait(driver,3).until(
                expected_conditions.presence_of_element_located(
                    (By.CSS_SELECTOR, 'button[aria-label="OK"]')
                )
            )
            onlineclassscript()
        except:
            try:
                match_search = WebDriverWait(driver,117).until(
                    expected_conditions.presence_of_element_located(
                        (By.CSS_SELECTOR, 'div[class*="pollingContainer"]')
                    )
                )
                try:
                    search = driver.find_element_by_css_selector('button[aria-label="'+poll+'"]')
                    time.sleep(8)
                    search.click()
                except Exception as e:
                    search = driver.find_element_by_css_selector('button[aria-label="Yes"]')
                    time.sleep(5)
                    search.click()
            except Exception as e:
                pass

onlineclassscript()
