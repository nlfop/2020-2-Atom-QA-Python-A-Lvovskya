import http.server
from http.server import HTTPServer
import threading
from io import BytesIO
import os

PORT = 9000

def authorization(data):
    if (data[1:5]=='user')&(data[14:18]=='pass'):
        if (data[7:12]=='admin')&(data[20:]=='123'):
            return 'Success authorization'
        else:
            return 'Error with authorization'

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        data = self.translate_path(self.path)
        if (data[-9:])=='login.php':
            result = authorization(self.rfile.read(content_length).decode())
            if result == 'Success authorization':
                self._set_response()
                return
            else:
                self.send_error(404)
                return
        else:
            self.send_error(405)
            self.send_response(405, "Method Not Allowed")
            return


    def do_PUT(self):
        path = self.translate_path(self.path)
        print(path)
        if path.endswith('/'):
            self.send_response(500, "Method Not Allowed")
            self.send_error(500)
            self.wfile.write("PUT not allowed on a directory\n".encode())
            return
        else:
            try:
                os.makedirs(os.path.dirname(path))
            except FileExistsError:
                pass

            length = int(self.headers['Content-Length'])
            with open(path, 'wb') as f:
                f.write(self.rfile.read(length))
            self.send_response(201, "Created")
            self.send_header('Content-type', 'text/html')
            self.end_headers()


class MockServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.stop_server = False
        self.handler = MyHttpRequestHandler
        self.handler.data = None
        self.server = HTTPServer((self.host, self.port), self.handler)

    def start(self):
        self.server.allow_reuse_address = True
        th = threading.Thread(target=self.server.serve_forever, daemon=True)
        th.start()
        return self.server

    def stop(self):
        self.server.server_close()
        self.server.shutdown()

