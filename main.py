from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:/Users/cantu/appdata/local/Chromium/User Data/")
s=Service('C:/Users/cantu/Documents/chromedriver.exe')
driver = webdriver.Chrome(service=s,options=options)

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

target = '"Tek başına"'

string = "deneme 1 2 3"

x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((
    By.XPATH, x_arg)))
group_title.click()
inp_xpath = '//div[@class="_13NKt copyable-text selectable-text"][@data-tab="10"]'

input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, inp_xpath)))
for i in range(4):
    input_box.send_keys(string + Keys.ENTER)
    time.sleep(0.5)