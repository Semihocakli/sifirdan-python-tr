# Python'da Web Programlama ve API Kullanımı
# =====================================

"""
WEB PROGRAMLAMA VE API NEDİR?
--------------------------
Web programlama, web uygulamaları geliştirmeyi ve internet üzerinden 
veri alışverişi yapmayı sağlar. API (Application Programming Interface) 
ise farklı yazılımların birbiriyle iletişim kurmasını sağlayan arayüzdür.

Bu dosyada:
1. Basit bir web sunucusu oluşturma
2. HTTP istekleri yapma
3. REST API kullanımı
4. JSON veri işleme
konularını işleyeceğiz.
"""

import http.server
import socketserver
import json
import requests
from typing import Dict, Any
from datetime import datetime
import threading

# 1. BASİT WEB SUNUCUSU
# -------------------
print("1. Basit Web Sunucusu:")

class BasitHandler(http.server.SimpleHTTPRequestHandler):
    """Basit HTTP isteklerini işleyen sınıf."""
    
    def do_GET(self):
        """GET isteklerini işler."""
        if self.path == '/':
            # Ana sayfa
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            
            html = """
            <html>
            <head>
                <title>Python Web Sunucusu</title>
                <style>
                    body { font-family: Arial; margin: 40px; }
                    h1 { color: #2c3e50; }
                    .menu { background: #ecf0f1; padding: 20px; }
                </style>
            </head>
            <body>
                <h1>Python Web Sunucusu</h1>
                <div class="menu">
                    <p>Mevcut sayfalar:</p>
                    <ul>
                        <li><a href="/saat">/saat - Güncel saat</a></li>
                        <li><a href="/selam/Python">/selam/[isim] - Selamlama</a></li>
                    </ul>
                </div>
            </body>
            </html>
            """
            self.wfile.write(html.encode('utf-8'))
            
        elif self.path == '/saat':
            # Saat sayfası
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            
            simdi = datetime.now().strftime("%H:%M:%S")
            self.wfile.write(f"Şu anki saat: {simdi}".encode('utf-8'))
            
        elif self.path.startswith('/selam/'):
            # Selamlama sayfası
            isim = self.path.split('/')[-1]
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            
            self.wfile.write(f"Merhaba, {isim}!".encode('utf-8'))
            
        else:
            # 404 Sayfa Bulunamadı
            self.send_response(404)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            
            self.wfile.write("Sayfa bulunamadı!".encode('utf-8'))

def sunucu_baslat(port: int = 8000):
    """Web sunucusunu başlatır."""
    handler = BasitHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Sunucu port {port}'da başlatıldı...")
        httpd.serve_forever()

# Sunucuyu arka planda başlat
sunucu_thread = threading.Thread(target=sunucu_baslat)
sunucu_thread.daemon = True  # Ana program bitince sunucu da kapanır
sunucu_thread.start()

# 2. HTTP İSTEKLERİ
# ---------------
print("\n2. HTTP İstekleri:")

def hava_durumu_getir(sehir: str) -> Dict[str, Any]:
    """OpenWeatherMap API'sini kullanarak hava durumu bilgisi getirir."""
    # Not: Gerçek API anahtarı almanız gerekir
    API_KEY = "your_api_key_here"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": sehir,
        "appid": API_KEY,
        "units": "metric",
        "lang": "tr"
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Hata kontrolü
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Örnek API isteği
print("Hava Durumu API Örneği:")
# print(json.dumps(hava_durumu_getir("Istanbul"), indent=2, ensure_ascii=False))

# 3. REST API OLUŞTURMA
# ------------------
print("\n3. REST API Örneği:")

class APIHandler(http.server.BaseHTTPRequestHandler):
    """REST API isteklerini işleyen sınıf."""
    
    def _send_json_response(self, data: Dict[str, Any], status: int = 200):
        """JSON formatında yanıt gönderir."""
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))
    
    def do_GET(self):
        """GET isteklerini işler."""
        if self.path == '/api/zaman':
            data = {
                "timestamp": datetime.now().isoformat(),
                "message": "Başarılı"
            }
            self._send_json_response(data)
        else:
            self._send_json_response({"error": "Endpoint bulunamadı"}, 404)
    
    def do_POST(self):
        """POST isteklerini işler."""
        if self.path == '/api/echo':
            # İstek gövdesini oku
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                # JSON verisini işle
                data = json.loads(post_data.decode('utf-8'))
                self._send_json_response({
                    "received": data,
                    "message": "Veri alındı"
                })
            except json.JSONDecodeError:
                self._send_json_response({
                    "error": "Geçersiz JSON verisi"
                }, 400)
        else:
            self._send_json_response({"error": "Endpoint bulunamadı"}, 404)

# 4. API KULLANIM ÖRNEKLERİ
# ----------------------
print("\n4. API Kullanım Örnekleri:")

def api_istekleri():
    """Çeşitli API istekleri örnekleri."""
    # GET isteği
    response = requests.get('http://localhost:8000/api/zaman')
    print("GET /api/zaman:", response.json())
    
    # POST isteği
    data = {"mesaj": "Merhaba, API!"}
    response = requests.post('http://localhost:8000/api/echo', json=data)
    print("POST /api/echo:", response.json())
    
    # Hata durumu
    response = requests.get('http://localhost:8000/api/var-olmayan')
    print("GET /api/var-olmayan:", response.json())

"""
WEB PROGRAMLAMA İPUÇLARI
----------------------
1. CORS (Cross-Origin Resource Sharing) ayarlarına dikkat edin
2. API endpoint'lerini doğru tasarlayın
3. İstekleri ve yanıtları doğrulayın
4. Rate limiting uygulayın
5. API dokümantasyonu hazırlayın

GÜVENLİK ÖNLEMLERİ
----------------
1. API anahtarlarını gizli tutun
2. HTTPS kullanın
3. Input validasyonu yapın
4. Rate limiting uygulayın
5. Hata mesajlarında hassas bilgi vermeyin

PERFORMANS İPUÇLARI
----------------
1. Önbellek (cache) kullanın
2. Asenkron istekler yapın
3. Bağlantı havuzu kullanın
4. Gereksiz isteklerden kaçının
5. Yanıt boyutunu optimize edin
"""

if __name__ == "__main__":
    # Ana program burada başlar
    print("Web sunucusu ve API örnekleri hazır...")
    print("http://localhost:8000 adresini ziyaret edin")
    
    # Programın kapanmaması için bekle
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nProgram sonlandırılıyor...") 