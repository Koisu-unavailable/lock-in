from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import threading
from utils.StoppableThread import StoppableThread
import time
HOSTNAME = "localhost"
SERVERPORT = 6969
logger = logging.Logger("ConfigServer", logging.DEBUG)
class ConfigServer(BaseHTTPRequestHandler):
    def do_GET(self):
        logger.debug("GETTONG FILE")
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        print(self.path.split("/"))
        if self.path.split("/")[1] == "file":
            with open(self.path.removeprefix("/file/"), "r") as file:
                print("here")
                self.wfile.write(bytes(file.read(), "utf-8"))

def get_config_server_thread():
    thread = StoppableThread(target=_start_server, name="Server")
    return thread
def _start_server(event: threading.Event):
    server = HTTPServer((HOSTNAME, SERVERPORT), ConfigServer)
    print('HERE FIRST')
    logger.debug(f"Server started http://{HOSTNAME}:{SERVERPORT}")
    print('here')
    server.serve_forever()
    while True:
        time.sleep(1)
        if event.is_set():
            print("here")
            server.server_close()
            logger.debug("Server stopped")

    
