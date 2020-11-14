import os
from selenium import webdriver

# URL
url_parent = 'https://enact-parent.github.io/server-parent/staticpages/ver87/scenario1/parent.html'

# chromedriver 경로를 얻습니다 (ver87)
driver_path = os.getcwd() + '/../chromedriver87'

# selenium 으로 Chrome 실행 시 적용할 Args 를 설정합니다
options = webdriver.ChromeOptions()
options.add_argument('--disable-web-security')
options.add_argument('--disable-site-isolation-trials')

# parent.html 을 열 driver 를 얻습니다
driver_parent = webdriver.Chrome(driver_path, options=options)

# driver 로 페이지를 엽니다
driver_parent.get(url_parent)


