import http.server
import socketserver

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'sample.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


handler = MyHttpRequestHandler
PORT = 8000
my_server = socketserver.TCPServer(('', PORT), handler)
my_server.serve_forever()
