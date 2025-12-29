from http.server import BaseHTTPRequestHandler, HTTPServer
import os

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

class UploadHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"""
        <html><body>
        <h2>Upload File</h2>
        <form method="POST" enctype="multipart/form-data">
            <input type="file" name="file" required>
            <input type="submit" value="Upload">
        </form>
        </body></html>
        """)

    def do_POST(self):
        length = int(self.headers['Content-Length'])
        data = self.rfile.read(length)

        boundary = self.headers['Content-Type'].split("boundary=")[1].encode()
        parts = data.split(boundary)

        for part in parts:
            if b'Content-Disposition' in part:
                header, filedata = part.split(b'\r\n\r\n', 1)
                filedata = filedata.rstrip(b'\r\n--')

                for line in header.split(b'\r\n'):
                    if b'filename=' in line:
                        filename = line.split(b'filename=')[1].strip(b'"')

                with open(os.path.join(UPLOAD_DIR, filename.decode()), 'wb') as f:
                    f.write(filedata)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Upload successful")

server = HTTPServer(("0.0.0.0", 5555), UploadHandler)
print("Server running on port 5555")
server.serve_forever()
