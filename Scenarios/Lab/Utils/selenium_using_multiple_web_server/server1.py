import http.server
import socketserver

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'sample1.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


handler = Handler
PORT = 8001
server1 = socketserver.TCPServer(('', PORT), handler)
