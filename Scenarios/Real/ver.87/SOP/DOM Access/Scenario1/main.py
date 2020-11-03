import os
from socketserver import TCPServer
from selenium import webdriver
from threading import Thread
from child import Child
from parent import Parent

server_parent = TCPServer(('', Parent.PORT), Parent.Handler)
server_child = TCPServer(('', Child.PORT), Child.Handler)

th1 = Thread(target=server_parent.serve_forever)
th2 = Thread(target=server_child.serve_forever)

th1.daemon = True
th2.daemon = True

th1.start()
th2.start()

while not th1.is_alive() or not th2.is_alive():
    continue

driver_path = os.getcwd() + '/chromedriver87'
options = webdriver.ChromeOptions()
options.add_argument('--disable-web-security')
options.add_argument('--disable-site-isolation-trials')
driver_parent = webdriver.Chrome(driver_path, options=options)
driver_parent.get('localhost:8001')


