import time

from selenium import webdriver

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


PATH = "../../Classes/chromedriver"
MEET = "bct-fmjc-etn"
NAME = "Ashu"

opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 2,
    "profile.default_content_setting_values.media_stream_camera": 2,
    "profile.default_content_setting_values.geolocation": 0,
    "profile.default_content_setting_values.notifications": 1
})

driver = webdriver.Chrome(options=opt,executable_path=PATH)

def attendance():

    driver.get("https://meet.google.com/"+MEET)
    # Dismiss the Popup

    dialog_box = WebDriverWait(driver,7).until(
        expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, 'div[role="alertdialog"]')
        )
    )
    dismiss_btn = dialog_box.find_element(by=By.TAG_NAME,value="button")
    dismiss_btn.click()

    name_in = driver.find_element(by=By.CSS_SELECTOR, value='input[aria-label="Your name"]')
    name_in.send_keys(NAME)
    name_in.send_keys(Keys.ENTER)

    try:
        match_search = WebDriverWait(driver,5).until(
            expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, 'div[role="alertdialog"]')
            )
        )
    except Exception as e:
        # print(e)
        attendance()


attendance()

        

