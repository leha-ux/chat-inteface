from http.server import HTTPServer, BaseHTTPRequestHandler
import logging
logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

class myHandler(BaseHTTPRequestHandler):
    def do_GET(self): 
        logging.info("Test")
        if self.path.endswith("/error"):
            self.send_response(500)
        else:
            self.send_response(200)
            self.send_header('context-type', 'text-html')
            self.end_headers()
            self.wfile.write(self.path.encode())
    
    def do_POST(self):
        logging.info("Test")
        length = int(self.headers['Content-Length'])
        print("Test")
        body = self.rfile.read(length)
        self.send_response(200)
        self.end_headers()
        self.wfile.write((body))



def main():
    PORT=8082
    server = HTTPServer(('', PORT), myHandler)
    print("Server running forever")
    try: 
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    server.server_close()
    print("ENd")
if __name__ == '__main__':
    main()