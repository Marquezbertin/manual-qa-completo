# 07/scripts/target_server.py
"""Alvo local (stdlib) para os testes de carga Locust/k6.

Sobe em http://127.0.0.1:8080 e responde JSON em:
  GET  /produtos/1
  POST /checkout   (body JSON {"item": int, "qtd": int})
"""
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class Handler(BaseHTTPRequestHandler):
    def _send(self, code, obj):
        body = json.dumps(obj).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path.startswith("/produtos/"):
            pid = self.path.split("/")[-1]
            return self._send(200, {"id": pid, "nome": "Produto", "preco": 10.0})
        return self._send(404, {"error": "not found"})

    def do_POST(self):
        if self.path == "/checkout":
            length = int(self.headers.get("Content-Length", 0))
            data = json.loads(self.rfile.read(length) or b"{}")
            return self._send(200, {"ok": True, "item": data.get("item")})
        return self._send(404, {"error": "not found"})

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", 8080), Handler)
    print("Target server em http://127.0.0.1:8080")
    server.serve_forever()
