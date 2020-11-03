import http.server

class Handler2(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'child.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


handler = Handler2
