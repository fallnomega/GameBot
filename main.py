from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option("detach",True)
chrome_driver = 'chromedriverDirectory'
driver = webdriver.Chrome(executable_path=chrome_driver, options=options)
driver.get('http://orteil.dashnet.org/experiments/cookie/')
# language = driver.find_element(By.XPATH,'//*[@id="langSelect-EN"]')
the_cookie = driver.find_element(By.ID,'cookie')
the_cookie.click()
# print(language.text)
# the_cookie = driver.find_element(By.XPATH,'//*[@id="bigCookie"]')

# driver.close() #clses the tab the driver opens

# for x in range(100):
#     the_cookie.click()

