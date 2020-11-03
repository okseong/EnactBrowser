import os
import socketserver
from selenium import webdriver
from threading import Thread
from server1 import Handler1
from server2 import Handler2

PORT_PARENT = 8001
PORT_CHILD = 8002

server_parent = socketserver.TCPServer(('', PORT_PARENT), Handler1)
server_child = socketserver.TCPServer(('', PORT_CHILD), Handler2)

th1 = Thread(target=server_parent.serve_forever)
th2 = Thread(target=server_child.serve_forever)

th1.daemon = True
th2.daemon = True

th1.start()
th2.start()

while not th1.is_alive() or not th2.is_alive():
    continue

path = os.getcwd() + '/../../chromedriver87'
options = webdriver.ChromeOptions()
options.add_argument('--disable-web-security')
options.add_argument('--disable-site-isolation-trials')
driver1 = webdriver.Chrome(path, options=options)
driver2 = webdriver.Chrome(path, options=options)
driver1.get('localhost:8001')
driver2.get('localhost:8002')
