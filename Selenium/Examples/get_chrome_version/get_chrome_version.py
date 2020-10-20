import os
from selenium import webdriver

driver_path = os.getcwd() + '/chromedriver'
driver = webdriver.Chrome(driver_path)

driver.get('chrome://version')
elem = driver.find_element_by_css_selector('#version > span:nth-child(1)')

print('Chrome version :', elem.text)
