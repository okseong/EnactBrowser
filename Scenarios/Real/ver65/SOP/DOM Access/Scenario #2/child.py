import http.server

class ChildHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'child.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


class Child:
    Handler = ChildHandler
    PORT = 8002

