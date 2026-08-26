# 06/scripts/app.py
"""Mini API REST offline (apenas stdlib) para os testes do Módulo 06.

Implementa GET /posts/<id>, POST /posts e 404 para o resto.
Não é produção: serve apenas de alvo real e local para os testes.
"""
import json
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

POSTS = {1: {"userId": 1, "id": 1, "title": "hello", "body": "world"}}


class Handler(BaseHTTPRequestHandler):
    def _send(self, code, obj):
        body = json.dumps(obj).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path.startswith("/posts/"):
            try:
                pid = int(self.path.split("/")[-1])
            except ValueError:
                return self._send(404, {"error": "not found"})
            post = POSTS.get(pid)
            if post is None:
                return self._send(404, {"error": "not found"})
            return self._send(200, post)
        return self._send(404, {"error": "not found"})

    def do_POST(self):
        if self.path == "/posts":
            length = int(self.headers.get("Content-Length", 0))
            raw = self.rfile.read(length) if length else b"{}"
            data = json.loads(raw or b"{}")
            new_id = max(POSTS) + 1
            post = {
                "userId": data.get("userId", 0),
                "id": new_id,
                "title": data.get("title", ""),
                "body": data.get("body", ""),
            }
            POSTS[new_id] = post
            return self._send(201, post)
        return self._send(404, {"error": "not found"})

    def log_message(self, *args):
        pass


def start_server(port=0):
    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server
