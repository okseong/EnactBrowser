import os
from socketserver import TCPServer
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys
from threading import Thread

def main():
    chrome_options = ChromeOptions()
    # chrome_options.add_argument('--disable-web-security')
    # chrome_options.add_argument('--disable-site-isolation-trials')
    chrome_driver_path = os.path.join(os.getcwd(), 'chromedriver_linux64/chromedriver')
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver_path)

    driver.get("https://pullup-dip-burpee.github.io/my-first-blog/Squat.html")
    h1_elem = driver.find_element_by_tag_name('h1')
    print(h1_elem)

    # atb = driver.find_element_by_xpath("//input[@id='']/parent::div")
    # val = atb.get_attribute("class")
    # print(val)
    driver.close()

if __name__ == '__main__':
    main()