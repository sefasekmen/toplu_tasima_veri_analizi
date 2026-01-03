# Başlarken

Bu proje, İstanbul'un Eylül 2024 toplu taşıma verilerini analiz etmektedir.

## Kurulum

### 1. Gerekli Kütüphaneleri Yükleyin

```bash
pip install -r requirements.txt
```

Veya tek tek:
```bash
pip install pandas matplotlib seaborn numpy
```

### 2. Veri Dosyasını Hazırlayın

CSV dosyası `4546fb79-e598-4dc7-888b-626361110e37.csv` adında olmalı ve `main.py` ile aynı klasörde bulunmalıdır.

İndirme bağlantısı (İBB Açık Veri):
https://data.ibb.gov.tr/dataset/hourly-public-transport-data-set/resource/4546fb79-e598-4dc7-888b-626361110e37

### 3. Programı Çalıştırın

```bash
python main.py
```

Windows'ta Türkçe karakterleri doğru göstermek için:
```bash
$env:PYTHONIOENCODING='utf-8'; python main.py
```

## Çıktılar

Program çalışırken:

1. **Konsola çıktı**: Saatlik, günlük, ilçe, hat gibi analizlerin özeti yazılır
2. **Grafik dosyası**: `grafik_analizi.png` adında 15 grafik içeren bir PNG dosyası oluşturulur

## Dosya Yapısı

```
├── main.py                    # Ana Python kodu
├── requirements.txt           # Kütüphane listesi
├── README.md                  # Detaylı rapor
├── ANALIZ.md                  # Grafik analizleri
├── BASLARKEN.md               # Bu dosya
├── INDEX.md                   # Proje özeti
├── .gitignore                 # Git ayarları
├── grafik_analizi.png         # Çıktı grafikleri
└── 4546fb79...csv            # Veri dosyası
```

## Kod Yapısı

### 1. Veri Yükleme
```python
df = pd.read_csv('dosya_ismi')
```

### 2. Veri Temizleme ve İşleme
- Tarih sütunlarını datetime'a çevirme
- Gün isimlerini Türkçeye çevirme
- Hafta içi/hafta sonu kategorisi oluşturma

### 3. Analizler
Pandas groupby, pivot_table ve agg fonksiyonları kullanarak:
- Saatlik yoğunluk
- Günlük yoğunluk
- Taşımacılık türü dağılımı
- İlçe analizleri
- Hat analizleri
- Transfer analizleri

### 4. Görsellendirme
Matplotlib ve Seaborn kullanarak:
- Line charts (çizgi grafikler)
- Bar charts (bar grafikler)
- Pie charts (pasta grafikler)
- Heatmaps (ısı haritaları)
- Error bars (hata çubukları)

## Grafikler Hakkında

15 grafik oluşturulur:

1. **Saatlik Yolcu Trafiği** - Zaman serisine göre trafik değişimi
2. **Günlük Yolcu Dağılımı** - Hangi gün ne kadar yoğun
3. **Taşımacılık Türü Pazar Payı** - Otobüs vs Metro vs Vapur
4. **Taşımacılık Türü × Saat Haritası** - Hangi saatte hangi tür yoğun
5. **Hafta İçi vs Hafta Sonu** - Karşılaştırmalı analiz
6. **Top 10 İlçe** - En yoğun ilçeler
7. **Top 10 Hat** - En yoğun hatlar
8. **Bilet Türü Dağılımı** - Tam, İndirimli, Ücretsiz
9. **Transfer Türü Dağılımı** - Normal vs Aktarma
10. **Günlük Trend** - Aylar içinde yolcu sayısı değişimi
11. **Saatlik Taşımacılık Dağılımı** - Stacked bar chart
12. **İşlem Türü Dağılımı** - Kontur vs Abonman vs Aktarma
13. **Saatlik Ort. Yolcu** - Error bar ile tutarlılık analizi
14. **Gün × Saat Haritası** - 2D heatmap
15. **Standart Sapma** - Tahmincililik analizi

## Veri Kaynağı

İstanbul Büyükşehir Belediyesi Açık Veri Portalı

## Not

Veriler 1-10 Eylül 2024 tarihlerini kapsamaktadır ve veri dengesizliği olabilir (özellikle günler arasında).

## Lisans

Bu proje eğitim amaçlı yapılmıştır ve açık kaynak politikasına uyacak şekilde paylaşılmaktadır.
