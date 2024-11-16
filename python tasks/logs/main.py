import json
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime

LOG_DIR = "logs/server.log"

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        client_ip = self.client_address[0]
        method = self.command
        request_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        response_content = {
            "client_ip": client_ip,
            "method": method,
            "request_time": request_time,
        }

        print(response_content)

        with open(LOG_DIR, "a") as f:
            f.write(json.dumps(response_content)+"\n")

        logs = []
        try:
            with open(LOG_DIR, "r") as f:
                for line in f:
                    try:
                        details = json.loads(line.strip())
                        logs.append(details)
                    except json.JSONDecodeError:
                        continue
        except FileNotFoundError:
            self.send_error(500, "Log fayli topilmadi.")
            return
        

        count_requests = sum(1 for log in logs if log["client_ip"] == client_ip)

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        response = json.dumps({"count_requests": count_requests})
        self.wfile.write(response.encode())


PORT = 8000
server_address = ("", PORT)
httpd = HTTPServer(server_address, MyRequestHandler)

print(f"Server running at http://localhost:{PORT}")
httpd.serve_forever()
