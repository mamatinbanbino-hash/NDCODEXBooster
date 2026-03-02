from http.server import BaseHTTPRequestHandler
import json
import random

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)
        
        target = data.get("url", "Inconnu")
        mode = data.get("type", "BOOST")

        # Logique de réponse
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        res = {
            "status": "PROTOCOLE_ACTIF_100%",
            "message": f"Injection de 1000 {mode} lancée sur {target[:20]}...",
            "session": f"ID-{random.randint(100000, 999999)}"
        }
        
        self.wfile.write(json.dumps(res).encode('utf-8'))
