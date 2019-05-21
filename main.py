from http.server import HTTPServer, BaseHTTPRequestHandler

from io import BytesIO

from random import randint

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Send post request with body of "house/sensor,get_temp" to get current temp')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        split = body.decode().split(",")
        response = BytesIO()
        if split[0] == "house/sensor" and split[1] == "get_temp":
            self.send_response(200)
            self.end_headers()
            temp = randint(30,45)    
            response.write(str(temp).encode())
            print("received message=" + body.decode() + ", topic=" + split[0] +". Sent temp="+str(temp))
        else:
            self.send_response(400)
        self.wfile.write(response.getvalue())
        

httpd = HTTPServer(("", 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()