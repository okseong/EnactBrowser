import os
from socketserver import TCPServer
from selenium import webdriver
from threading import Thread
from child import Child
from parent import Parent

# parent 의 server 와 child 의 server 를 생성합니다
server_parent = TCPServer(('', Parent.PORT), Parent.Handler)
server_child = TCPServer(('', Child.PORT), Child.Handler)

# server 를 실행시킬 thread 들을 생성합니다
th1 = Thread(target=server_parent.serve_forever)
th2 = Thread(target=server_child.serve_forever)

# main.py 가 종료되면 thread 도 같이 종료되도록 합니다
# 종료되는데 시간이 걸릴 수 있습니다
# lsof -i tcp:<Child.PORT>, lsof -i tcp:<Parent.PORT> 로
# 현재 서버가 실행되고 있는지 확인할 수 있습니다
th1.daeon = True
th2.daemon = True

# thread 들을 실행시킵니다
th1.start()
th2.start()

# thread 들을 통해 server 가 실행될 때까지 기다립니다
while not th1.is_alive() or not th2.is_alive():
    continue

# chromedriver 경로를 얻습니다 (ver87)
driver_path = os.getcwd() + '/../chromedriver87'

# selenium 으로 Chrome 실행 시 적용할 Args 를 설정합니다
options = webdriver.ChromeOptions()
options.add_argument('--disable-web-security')
options.add_argument('--disable-site-isolation-trials')

# localhost:8001 에 서비스되고 있는 parent.html 을 열 driver_parent 를 얻습니다
# localhost:8002 에 서비스되고 있는 parent.html 을 열 driver_child 를 얻습니다
driver_parent = webdriver.Chrome(driver_path, options=options)
driver_child = webdriver.Chrome(driver_path, options=options)

# driver 들로 각 페이지를 엽니다
driver_parent.get('localhost:8001')
driver_child.get('localhost:8002')


