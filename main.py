from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import re


def find_max_item_to_buy(the_options,my_bank):
    name = []
    value = []
    for x in the_options:
        if my_bank >= float(x[1].replace(',', '')):
            name.append(x[0])
            value.append(int(x[1].replace(',', '')))
    max_value = max(value)
    max_location = value.index(max_value)
    return [name[max_location], value[max_location]]

options = Options()
options.add_experimental_option("detach", True)
chrome_driver = 'chromedriverDirectory'
driver = webdriver.Chrome(executable_path=chrome_driver, options=options)
driver.get('http://orteil.dashnet.org/experiments/cookie/')
the_cookie = driver.find_element(By.ID, 'cookie')
buy_options = driver.find_element(By.ID, 'store')
temp = buy_options.text.split('\n')
selections = [re.split('\n.*\n', x) for x in temp]
del selections[1::2]
my_choices = [x[0].split(' - ') for x in selections]

keep_alive = True
sentinal = 0
while keep_alive:
    the_cookie.click()
    t_end = time.time() + 5
    while time.time() < t_end:
        the_cookie.click()
    time.sleep(2)
    my_money = driver.find_element(By.ID, 'money')
    my_money = my_money.text.replace(',','')
    my_money = int(my_money)
    buying = find_max_item_to_buy(my_choices,my_money)
    get_upgrade = driver.find_element(By.ID, f'buy{buying[0]}')
    get_upgrade.click()
    sentinal += 1
    if sentinal >= 5:
        keep_alive = False
time.sleep(2)
cookies_per_second = driver.find_element(By.ID,'cps')
print(f"cookies per second: {cookies_per_second.text}")