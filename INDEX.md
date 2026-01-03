# Proje Özeti

Bu klasördeki dosyalar şunlardır:

## 📄 Belge Dosyaları

- **README.md** (15 KB) - Ana rapor. Saatlik analiz, günlük analiz, taşımacılık türü, bilet türü, ilçe, hat, işlem türü, transfer ve trendler hakkında detaylı yorumlar içerir. GitHub'da bu dosya otomatik gösterilir.

- **ANALIZ.md** (10 KB) - Grafikler hakkında detaylı yorumlar. Her bir grafiğin ne gösterdiği, nasıl yorumlanması gerektiği yazılıdır.

- **BASLARKEN.md** (3 KB) - Kurulum ve çalıştırma talimatları. Python'u bilmeyen kişiler için step by step yapı anlatılır.

## 💻 Kod Dosyaları

- **main.py** (13 KB) - Ana Python kodu. Veri yükleme, temizleme, analiz ve grafik oluşturma işlemleri burada yapılır. Öğrenci seviyesine uygun düz ve anlaşılır yazılmıştır.

- **requirements.txt** - Kütüphane lisesi. `pip install -r requirements.txt` komutuyla tüm gerekli paketler yüklenir.

## 📊 Veri Dosyaları

- **4546fb79-e598-4dc7-888b-626361110e37.csv** (365 MB) - İstanbul toplu taşıma Eylül 2024 verileri. 3.52 milyon satır, 39.3 milyon yolcu.

## 📈 Grafik Dosyaları

- **grafik_analizi.png** (1.3 MB) - 15 farklı grafik içeren çıktı. Yüksek çözünürlük (300 DPI).

## ⚙️ Konfigürasyon

- **.gitignore** - GitHub'a yüklenmemesi gereken dosyalar (CSV ve PNG gibi büyük dosyalar).

## Proje Hiyerarşisi

```
toplu_tasima_veri_analizi/
│
├── main.py                              # Ana program
├── requirements.txt                     # Bağımlılıklar
│
├── README.md                            # Ana rapor
├── ANALIZ.md                            # Grafik analizleri
├── BASLARKEN.md                         # Kurulum rehberi
│
├── grafik_analizi.png                   # Çıktı grafikleri
│
├── 4546fb79-e598-4dc7-...csv           # Veri (365 MB - .gitignore'da)
└── .gitignore                           # Git konfigürasyonu
```

## Nasıl Kullanılır?

### Bilgisayarında Çalıştırmak

1. Python 3.10+ yüklü olduğundan emin ol
2. `pip install -r requirements.txt` çalıştır
3. `python main.py` çalıştır
4. Konsol çıktısını oku, grafikleri incele

### GitHub'a Yüklemek

1. `git init` (ilk defa ise)
2. `git add .` (tüm dosyaları ekle)
3. `git commit -m "İstanbul toplu taşıma analizi projesi"`
4. `git remote add origin <repository-url>`
5. `git push -u origin main`

Not: CSV ve PNG dosyaları `.gitignore` içinde olduğu için yüklenmeyecektir.

## Anahtar Bulgular

- **En yoğun saat**: 08:00 (3.36M yolcu)
- **En az yoğun saat**: 03:00 (15K yolcu)
- **Taşımacılık dağılımı**: Otobüs 53.7%, Metro 43.5%, Vapur 2.8%
- **En yoğun ilçe**: Bakırköy (32.4%)
- **En yoğun hat**: 34 otobüsü (9.3%)
- **Transfer oranı**: %89 direkt, %11 aktarma

## Teknik Detaylar

- **Python Versiyonu**: 3.12+
- **Kütüphaneler**: Pandas, Matplotlib, Seaborn, NumPy
- **Veri boyutu**: 3.52M satır, 13 sütun
- **Grafik sayısı**: 15
- **Analiz türleri**: Saatlik, günlük, taşımacılık türü, bilet, ilçe, hat, transfer, işlem, trend

## Notlar

- Veriler 1-10 Eylül 2024 tarihlerini kapsamaktadır
- Veri dengesizliği olabilir (günler eşit sayıda gözlem içermez)
- Ayın sonu verilerinde kesintiye işaret eden anomali var
- Detaylı analizler README.md'de yer almaktadır

---

**Hazırlayan**: Sefa Sekmen
**Proje Tarihi**: Ocak 2026
**Veri Kaynağı**: İstanbul Açık Veri Portalı
