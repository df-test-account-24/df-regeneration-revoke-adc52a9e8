"""Disposable localhost-only health fixture."""
from http.server import BaseHTTPRequestHandler, HTTPServer

PROOF_LABEL = "QUEUED_REVOKE_PROOF_A677A76068"

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/health":
            self.send_error(404)
            return
        self.send_response(200)
        self.end_headers()
        self.wfile.write(("ok " + PROOF_LABEL).encode())

if __name__ == "__main__":
    HTTPServer(("127.0.0.1", 8080), Handler).serve_forever()
