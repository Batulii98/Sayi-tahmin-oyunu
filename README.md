# Sayı Tahmin Oyunu

1 ile 10 arasında rastgele bir sayıyı tahmin etmeye dayalı browser tabanlı oyun. Python ile basit bir HTTP sunucu üzerinde çalışır.

## Özellikler

- 1-10 arasında rastgele sayı üretimi
- Tahmine göre "daha büyük / daha küçük" ipucu
- Doğru tahmin sonrası arka plan yeşile döner ve oyun otomatik sıfırlanır
- Karanlık tema, neon glow tasarım

## Nasıl Çalıştırılır

**Gereksinim:** Python 3

```bash
cd "sayı tahmin oyunu"
python server.py
```

Ardından tarayıcıda aç: [http://localhost:8000](http://localhost:8000)

## Dosya Yapısı

```
sayı tahmin oyunu/
├── index.html   # Oyun arayüzü (HTML + CSS + JS)
└── server.py    # Python HTTP sunucusu
```

## Nasıl Oynanır

1. Kutuya 1-10 arasında bir sayı gir
2. **Tahmin Et** butonuna tıkla
3. Yönlendirme ipuçlarını takip et
4. Doğru sayıyı bulunca oyun otomatik olarak sıfırlanır

## Teknolojiler

- Python 3 (`http.server`)
- HTML5 / CSS3 / Vanilla JavaScript
