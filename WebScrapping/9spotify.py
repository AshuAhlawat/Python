#spotify
username = "xxxxx@gmail.com"
password = "xxxxxxx"

#discord
username_d = "xxxxxx@gmail.com"
password_d = "xxxxxxxxxx"

#queue
queue = 20

from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options

opt = Options()
opt.add_argument("start-maximized")
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic":1,
})

driver = webdriver.Chrome("C:\ProgramData\chromedriver.exe",options=opt)
driver.get("https://accounts.spotify.com/en/login?continue=https:%2F%2Fopen.spotify.com%2F")

print(driver.title)

match = WebDriverWait(driver,3).until(
    EC.presence_of_element_located(
        (By.NAME, "username")
    )
)
search = driver.find_element_by_name("username")
search.send_keys(username)
search = driver.find_element_by_name("password")
search.send_keys(password)
search.send_keys(Keys.ENTER)

match = WebDriverWait(driver,7).until(
    EC.presence_of_element_located(
        (By.LINK_TEXT, "Liked Songs")
    )
)

search = driver.find_element_by_link_text("Liked Songs")
search.click()

match = WebDriverWait(driver,7).until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div[style="transform: translateY(0px);"]')
    )
)

import time
time.sleep(1.5)

songs_html = driver.find_elements_by_class_name('standalone-ellipsis-one-line')
randomn_list = []

for song in songs_html:
    randomn_list.append(song.get_attribute('textContent'))

data_list = randomn_list[-150:]

artist_list=data_list[1: :3]
song_list = data_list[ : :3]

driver.get('https://discord.com/login')

match = WebDriverWait(driver,3).until(
    EC.presence_of_element_located(
        (By.NAME, "email")
    )
)

search = driver.find_element_by_name("email")
search.send_keys(username_d)
search = driver.find_element_by_name("password")
search.send_keys(password_d)
search.send_keys(Keys.ENTER)

match = WebDriverWait(driver,10).until(
    EC.presence_of_element_located(
        (By.CLASS_NAME,"wrapper-25eVIn")
    )
)

search = driver.find_element_by_css_selector('div[role="treeitem"]')
search.click()

search = driver.find_element_by_link_text('Music N Chill')
search.click()

search = driver.find_element_by_link_text('music')
search.click()

search = driver.find_element_by_css_selector('div[aria-label="Message #music"]')

for i in range(queue):
    search.send_keys("-p " + song_list[i]+ " " +artist_list[i])
    search.send_keys(Keys.ENTER)
    time.sleep(0.7)


