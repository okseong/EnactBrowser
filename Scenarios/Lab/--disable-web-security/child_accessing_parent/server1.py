import http.server

class Handler1(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'parent.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


handler1 = Handler1
