import json
import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/images.json":
            files = [
                f for f in os.listdir("images")
                if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))
            ]
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(files).encode())
        else:
            super().do_GET()

    def do_PUT(self):
        if self.path == "/data.json":
            length = int(self.headers["Content-Length"])
            body = self.rfile.read(length)
            with open("data.json", "wb") as f:
                f.write(body)
            self.send_response(200)
            self.end_headers()

print("Custom gallery server running at http://localhost:8000")
HTTPServer(("localhost", 8000), Handler).serve_forever()
