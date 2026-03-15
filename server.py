from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import random

PORT = 8000
hedef_sayi = random.randint(1,10)

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):

        global hedef_sayi
        sonuc = ""
        kazandi = "false"

        parsed_path = urllib.parse.urlparse(self.path)

        if parsed_path.path == "/tahmin":

            query = urllib.parse.parse_qs(parsed_path.query)
            tahmin = int(query.get("sayi", [0])[0])

            if tahmin < hedef_sayi:
                sonuc = "Daha büyük bir sayı dene!"

            elif tahmin > hedef_sayi:
                sonuc = "Daha küçük bir sayı dene!"

            else:
                sonuc = "Tebrikler! Doğru sayıyı buldun!"
                kazandi = "true"
                hedef_sayi = random.randint(1,10)

        self.send_response(200)
        self.send_header('Content-type','text/html; charset=utf-8')
        self.end_headers()

        with open("index.html","r",encoding="utf-8") as f:
            html = f.read()

        html = html.replace("{{sonuc}}", sonuc)
        html = html.replace("{{kazandi}}", kazandi)

        self.wfile.write(html.encode("utf-8"))

with HTTPServer(("",PORT),Handler) as server:
    print("Site çalışıyor: http://localhost:8000")
    server.serve_forever()