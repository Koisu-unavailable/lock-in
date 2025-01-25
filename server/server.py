from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import threading
HOSTNAME = "localhost"
SERVERPORT = 6969
logger = logging.Logger("ConfigServer", logging.DEBUG)
class ConfigServer(BaseHTTPRequestHandler):
    def do_GET(self):
        
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        print(self.path.split("/"))
        if self.path.split("/")[1] == "file":
            with open(self.path.removeprefix("/file/"), "r") as file:
                print("here")
                self.wfile.write(bytes(file.read(), "utf-8"))

def get_config_server_thread():
    server = HTTPServer((HOSTNAME, SERVERPORT), ConfigServer)
    logger.debug(f"Server started http://{HOSTNAME}:{SERVERPORT}")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()
    logger.debug("Server stopped")