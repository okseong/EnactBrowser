import http.server

class ParentHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'parent.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


class Parent:
    Handler = ParentHandler
    PORT = 8001

