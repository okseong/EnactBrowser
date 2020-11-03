import http.server
import socketserver

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'child.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


handler = Handler
PORT = 8002
server_child = socketserver.TCPServer(('', PORT), handler)
