import os
from selenium import webdriver
from threading import Thread
from .server1 import server_parent
from .server2 import server_child

th1 = Thread(target=server_parent.serve_forever)
th2 = Thread(target=server_child.serve_forever)

th1.daemon = True
th2.daemon = True

th1.start()
th2.start()

while not th1.is_alive() or not th1.is_alive():
    continue

path = os.getcwd() + '/../../chromedriver65'
driver1 = webdriver.Chrome(path)
driver2 = webdriver.Chrome(path)
driver1.get('localhost:8001')
driver2.get('localhost:8002')
