from threading import Thread
from .server1 import server1
from .server2 import server2

th1 = Thread(target=server1.serve_forever)
th2 = Thread(target=server2.serve_forever)

th1.daemon = True
th2.daemon = True

th1.start()
th2.start()

