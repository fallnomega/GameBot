from selenium import webdriver

chrome_driver = 'chromedriverDirectory'

driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get('https://www.amazon.com')
# driver.close() #clses the tab the driver opens
# driver.quit() # closes out the browser.