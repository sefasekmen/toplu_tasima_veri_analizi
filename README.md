# İstanbul Toplu Taşıma Veri Analizi Projesi

Eylül 2024 verileri kullanarak İstanbul'un toplu taşıma sisteminin detaylı analizi yapılmıştır.

## Veri Seti Hakkında

- **Kaynak**: İstanbul Büyükşehir Belediyesi Açık Veri Portalı (İndirme linki: https://data.ibb.gov.tr/dataset/hourly-public-transport-data-set/resource/4546fb79-e598-4dc7-888b-626361110e37)
- **Tarih Aralığı**: 1 - 10 Eylül 2024
- **Toplam Kayıt**: 3.520.000 satır
- **Toplam Yolcu**: 39.305.039 kişi
- **Ortalama Günlük Yolcu**: 3.930.504 kişi

## Analiz Bulguları

### 1. SAATLIK TRAFİK ANALİZİ

#### En Yoğun ve En Az Yoğun Saatler
- **En yoğun saat**: 08:00 (3.364.674 yolcu)
- **En az yoğun saat**: 03:00 (15.114 yolcu)
- **Trafik farkı**: 223 kat daha yoğun

#### Sabah Zirvesi (Rush Hour)
Sabah saatleri, özellikle 07:00-09:00 arası **işe gidiş zamanı** nedeniyle çok yoğundur. Saat 08:00 tam zirvedir ve bu saatte bir önceki/sonraki saatlere göre yaklaşık %10-15 daha fazla insanın toplu taşımayı kullandığı görülmektedir. Bu durum, şehir merkezine doğru gidiş akışının sabah saatlerinde yoğunlaştığını göstermektedir.

#### Akşam Zirvesi
Akşam saatleri, özellikle 13:00-19:00 arası da yoğun bir dönemdir. Öğle arası (13:00-14:00) ve işten çıkış saatleri (17:00-19:00) belirgin şekilde yüksek yolcu sayısıyla dikkat çekmektedir. Akşam zirvesinin sabah zirvesinden daha geniş bir zaman aralığında yayılmış olması ilginçtir; bu, insanların işten çıkış saatleri konusunda daha değişken davrandığını gösterebilir.

#### Gece Saatleri
Gece yarısı (00:00-06:00) tüm sistem içerisinde en az yoğun dönemdir. Özellikle 03:00-04:00 arasında neredeyse hiç yolcu yoktur. Bu saat aralığında sadece gece vardiyasında çalışan insanlar, gece hayatından dönenler ve acil ulaşım gereksinimleri olan kişiler toplu taşımayı kullanmaktadır.

**Grafik 1 ve Grafik 13 (Saatlik Trafik Analizi):** Grafikler, saatlik trafik dalgalanmasını çok net bir şekilde göstermektedir. Çizgi grafiğinde mavi alan altı, en yoğun saatleri vurgularken, Grafik 13'te standart sapma hesaplaması, farklı günlerde aynı saatin ne kadar tutarlı yolcu sayısına sahip olduğunu göstermektedir.

---

### 2. GÜNLÜK TRAFIK ANALİZİ

#### Hafta İçi vs Hafta Sonu
- **Hafta İçi Ort.**: 12 yolcu/saat
- **Hafta Sonu Ort.**: 10 yolcu/saat
- **Fark**: -12.9%

Beklenmedik şekilde **hafta sonu trafik hafta içinden %12.9 daha azdır**. Bu, weekendlerde insanların ya daha az hareket ettiklerini ya da özel araç kullanmayı tercih ettiklerini gösterebilir.

#### Günlük Dağılım
- **En yoğun gün**: Pazar (7.056.846 yolcu)
- **En az yoğun gün**: Salı (1.713.136 yolcu)

Veriye baktığımızda, hafta günleri arasında çok ciddi farklılıklar var. Pazarın pazar dışı günlerden 4 kat daha yoğun olması dikkat çeken bir bulgudur. Bunu açıklamak için verinin tarihleri dikkatle incelemek gerekir: veriler 1-10 Eylül 2024'ü kapsamaktadır ve bu tarihler:

- 1 Eylül (Pazar)
- 2 Eylül (Pazartesi)
- 3 Eylül (Salı)
- ...
- 10 Eylül (Salı)

Pazar tek başına yüksek sayıda veri noktasına sahip (diğer günler 2-3 gün kadarken Pazar sadece 1 gün). Verilerin dağılımı eşit olmadığı için bu grafikte dikkat edilmelidir. Yani **hafta sonu vs hafta içi karşılaştırması bu veride güvenilir değildir**.

**Grafik 2 (Günlük Dağılım):** Cyan renkle (hafta içi) ve pembeyle (hafta sonu) gösterilen günler net bir şekilde görülmektedir. Grafiğin üstündeki rakamlar (M cinsinden) milyonlar göstermektedir ve veri dengesizliğini açıkça ortaya koymaktadır.

**Grafik 5 (Hafta İçi vs Hafta Sonu):** İki dönemin karşılaştırması yapılmıştır. Hafta sonu toplam yolcu sayısının nispeten daha düşük olduğunu görmekle birlikte, bu bulgu veri dengesizliği nedeniyle şüpheli kalmalıdır.

---

### 3. TAŞIMACILIM TÜRÜ ANALİZİ

İstanbul toplu taşıma sistemi üç ana türden oluşmaktadır:

| Türü | Yolcu Sayısı | Yüzde | Açıklama |
|------|:--:|:---:|----------|
| **OTOYOL** | 21.118.338 | 53.7% | Otobüs taşımacılığı |
| **RAYLI** | 17.093.659 | 43.5% | Metro, hafif raylı, tren |
| **DENİZ** | 1.093.042 | 2.8% | Vapur, feribot |

#### Otobüs Sisteminin Dominansı
Otobüsler İstanbul taşımacılığının **omurgasını** oluşturmaktadır. Yarıdan fazla yolcu (53.7%) otobüs kullanmaktadır. Bunun nedenleri:

1. **Geniş coğrafi yayılım**: Otobüs hatları şehrin hemen her yerine ulaşmaktadır
2. **Esneklik**: Hafif raylı sistemlerin olmadığı yerlerde otobüs ana ulaşım aracıdır
3. **Bilinirlik**: Halk otobüs ağını metro kadar iyi bilmektedir

#### Raylı Sistem (Metro, Tren)
Raylı sistem %43.5 pay ile ikinci sırada yer almaktadır. Metro ve Marmaray gibi raylı ulaşımlar:

1. **Hız avantajı**: Otobüslerden çok daha hızlıdır
2. **Puantualiite**: Trafik etkileyen harici faktörlere maruz kalmaz
3. **Yüksek kapasitesi**: Özellikle ana koridorlarda yoğun trafik taşıyabilir

Raylı sistem payının %43.5 olması, İstanbul'un modern toplu taşıma altyapısına sahip bir metropol olduğunu göstermektedir.

#### Deniz Taşımacılığı
Vapur ve feribot gibi deniz taşımacılığı sadece %2.8 oranında kalmıştır. Bu, özellikle:

1. **Kısıtlı rotalar**: Deniz tarafından ulaşılabilen sınırlı ilçeler
2. **Sabit sefer saatleri**: Otobüs kadar sıklık olmayan seferler
3. **Ücret**: Otobüs ve metrodan daha pahalı

Ancak, deniz tarafından ulaşılabilen Adalar, Balıklı, Anadolu Yakası gibi lokasyonlarda deniz taşımacılığı çok önemlidir.

**Grafik 3 (Pie Chart - Pazar Payı):** Üç türün oransal dağılımı çok net görülmektedir. Otobüsün açık farkla önde olduğu görülmektedir.

**Grafik 4 (Isı Haritası - Tür x Saat):** Bu grafik çok önemlidir çünkü hangi saatlerde hangi taşımacılık türünün daha yoğun olduğunu göstermektedir. Sabah saatleri raylı sistemi daha kırmızı görünüyor (daha yoğun), bu da işe gidenlerin hızlı raylı sistemleri tercih ettiğini göstermektedir. Akşam saatleri otobüs ve raylı sistemler arasında daha az fark görülmektedir.

**Grafik 11 (Stacked Bar - Saatlik Taşımacılık Dağılımı):** Saat saat her türün mutlak yolcu sayısının nasıl değiştiğini göstermektedir. Sabah saatleri toplam yoğunluğun yüksek olduğu gibi, her türün de yoğunlaştığı görülmektedir.

---

### 4. BİLET TÜRÜ ANALİZİ

| Bilet Türü | Yolcu Sayısı | Yüzde |
|---|:--:|:---:|
| Tam Bilet | 15.888.354 | 40.5% |
| İndirimli | 15.845.632 | 40.4% |
| Ücretsiz | 5.869.331 | 15.0% |
| İndirimli 2 | 1.526.167 | 3.9% |
| Personel | 129.407 | 0.3% |

**Tam bilet ve indirimli bilet neredeyse eşit orana sahiptir** (%40.5 vs %40.4). Bu, indirimli bilet kullanıcılarının (öğrenciler, yaşlılar, engelliler) normal kullanıcılar kadar önemli bir grup olduğunu göstermektedir.

Ücretsiz bilet (15.0%), muhtemelen sosyal yardım programları veya hükümet destekli uygulamalar yoluyla dağıtılmıştır. Bu oran, İstanbul'da sosyal destek politikasının ne kadar yaygın olduğunu göstermektedir.

---

### 5. İLÇE ANALİZİ

| İlçe | Yolcu Sayısı | Yüzde |
|---|:--:|:---:|
| **Bakırköy** | 12.701.126 | 32.4% |
| **Fatih** | 3.845.485 | 9.8% |
| **Üsküdar** | 1.970.643 | 5.0% |
| **Küçükçekmece** | 1.737.826 | 4.4% |
| **Kadıköy** | 1.722.014 | 4.4% |

**Bakırköy'ün dominansı çarpıcıdır**: Tüm yolcuların **üçte birinden fazlası** Bakırköy'de taşınmıştır. Bunun nedenleri:

1. **Ulaştırma merkezi**: Bakırköy, D-100 karayolunu takip eden otobüs hatlarının merkezi konumdadır
2. **Endüstriyel bölge**: Bakırköy'de fabrikalar ve işletmeler vardır
3. **Ticarî merkez**: Bağdat Caddesi ve çevresi ticari aktivitelerin yoğun olduğu bölgedir
4. **Veri sayımı yöntemi**: Mümkün ki "transition" (geçiş) noktaları Bakırköy'de yoğunlaştırılmıştır

Fatih'in ikinci sırada yer alması (%9.8) İstanbul'un en merkezi ve yoğun nüfuslu ilçelerinden birisi olduğunu göstermektedir. Tarihi yarımada ve Galata Kulesi çevresi turizm ve ticaretin merkezi konumdadır.

**Grafik 6 (Bar Chart - Top 10 İlçe):** Bu grafik, İstanbul'un nüfus yoğunluğu ve ticari aktivitelerinin coğrafi dağılımını göstermektedir. Bakırköy'ün diğer ilçelerden ne kadar fazla olduğu net görülmektedir.

---

### 6. HAT ANALİZİ

| Hat Adı | Yolcu Sayısı | Yüzde |
|---|:--:|:---:|
| **34 (Otobüs)** | 3.642.548 | 9.3% |
| **Marmaray (Tren)** | 3.323.449 | 8.5% |
| **M2 (Metro)** | 2.238.553 | 5.7% |
| **T1 (Tramvay)** | 1.929.803 | 4.9% |
| **M1 (Metro)** | 1.869.979 | 4.8% |

#### En Popüler Hat: 34 Otobüsü
34 numaralı otobüs hattı, İstanbul'un en yoğun otobüs hattıdır. Muhtemelen Anadolu Yakası'ndan Avrupa Yakası'na veya aksine uzun mesafe gidişler yapan hattır. Otobüs olmasına rağmen metro kadar yoğun olması, raylı sistemlerin ulaşamadığı bölgeler arası bağlantıyı sağladığını göstermektedir.

#### Marmaray (Tren)
Marmaray, 8.5% oranla ikinci en yoğun hattır. Boğaziçi altından geçerek Ayrılıbaş-Halkalı rotasını takip eden bu tren hattı, iki yakayı bağlayan temel güzergahtır. 

#### Metro Hatları
M2 (5.7%), M1 (4.8%), M5 (4.2%), M4 (4.0%) ve M7 (3.2%) sırası ile diğer ana metrolardır. Metro hatlarının birbirinden farklı yüzdelere sahip olması:

1. **Hat uzunluğu**: Bazı hatlar daha uzun ve daha fazla istasyona sahiptir
2. **Uçak noktası**: Bazı hatlar daha merkezi, bazıları daha çevresel konumdadır
3. **Transfer merkezi**: Bazı istasyonlar transfer düğümü olarak önemlidir (Taksim, Sultanhamam vb)

#### Tramvay Hatları
T1 tramvayı (4.9%), turizm rotasıyla da bilinir (Sultanhamam-Zeytinburnu). Merkezde seyreden bu hatt, turist ve yerel kullanıcılara hizmet vermektedir.

**Grafik 7 (Bar Chart - Top 10 Hat):** Hangi hatların en popüler olduğu gösterilmektedir. 34 otobüsü ve Marmaray'ın açık farkla öne çıktığı görülmektedir.

---

### 7. İŞLEM TÜRÜ ANALİZİ

| İşlem Türü | Yolcu Sayısı | Yüzde |
|---|:--:|:---:|
| Tam Kontur | 12.994.810 | 33.1% |
| İndirimli Abonman | 8.918.322 | 22.7% |
| Ücretsiz | 5.534.995 | 14.1% |
| İndirimli Kontur | 3.787.862 | 9.6% |
| Tam Aktarma | 2.833.541 | 7.2% |

"Kontur" ve "Abonman" terimlerinin açıklanması gerekir:
- **Kontur**: Bir seferle bir bölgede sınırlı hareket
- **Abonman**: Belirli bir dönem için sınırsız veya çok sayıda kullanım hakkı

Tam Kontur (33.1%) kullanıcıları, düzenli ve belli rotada hareket eden insanlardır (işçiler, öğrenciler vb). 

İndirimli Abonman (22.7%), öğrenci ve yaşlıların aylık kartı gibi programlar aracılığıyla sistemde çok yaygın kullanılmaktadır.

Tam Aktarma (7.2%) yüzdesinin nisbeten düşük olması, insanların aktarma yapmaktan ziyade direkt rotalar tercih ettiğini göstermektedir.

---

### 8. TRANSFER ANALİZİ

| Transfer Türü | Yolcu Sayısı | Yüzde |
|---|:--:|:---:|
| Normal | 35.006.857 | 89.2% |
| Aktarma | 4.298.182 | 10.9% |

**Yolcuların %89'ı bir aktarma yapmadan gidişini tamamlamıştır.** Bu çok olumlu bir bulgudur çünkü:

1. **Direkt rotalar yeterlidir**: Kişiler A noktasından B noktasına direkt gidebilmektedir
2. **Sistem entegrasyonu**: Otobüs, metro, tramvay gibi farklı sistemler arasında iyi koordinasyon vardır
3. **Zaman kazancı**: Aktarma yapmayarak seyahat süresi kısaltılmaktadır

%10.9'luk aktarma oranı normal ve makul bir seviyedir. Raylı sistemlerde (metrolarda özellikle) aktarma oranı daha yüksek olabilir.

**Grafik 9 (Pie Chart - Transfer Türü):** Normal ve aktarma yapanların oranı görülmektedir. Yeşil alan (Normal) çok daha geniştir.

---

### 9. AYLIK TREND ANALİZİ

- **1 Eylül**: 3.462.341 yolcu
- **10 Eylül**: 1.711.396 yolcu
- **Değişim**: -50.6%

**Ayın sonuna doğru yolcu sayısında keskin bir düşüş gözlenmiştir.** (-50.6%)

Bu düşüşün nedenleri:

1. **Tarih aralığı yanlış seçilmiş olabilir**: 10 Eylül Salı günü olup, verilerin eksik kaydı veya kesik olma ihtimali vardır
2. **Okul tatili**: Eylülün ortasından itibaren öğretmen ve bazı öğrenciler tatil dönemi olabilir
3. **Veri kalitesi**: Verinin toplanma/kaydında sorun olabilir
4. **Kurban Bayramı arası**: Eylülde Kurban Bayramı olayını veya tatilini kontrol etmek gerekir

Bu trend şüpheli görülmektedir ve verinin tarihleriyle daha detaylı incelemesi gerekmektedir.

**Grafik 10 (Line Chart - Günlük Trend):** Günler geçtikçe kırmızı çizginin düşüşü açıkça görülmektedir. Başta 3.5M civarı olan yolcu sayısı, sona doğru 1.7M'ye düşmüştür.

---

### 10. SAATLIK ORTALAMA VE TUTARLILIK

**Grafik 13 (Error Bar - Standart Sapma):**

Bu grafik, her saat için kaç yolcu olduğunun sadece ortalama değil, ne kadar değişken olduğunu göstermektedir. Çubuklar ne kadar uzunsa, o saatте yolcu sayısı günler arasında o kadar tutarsızdır.

Sabah ve akşam saatleri düşük varyansa (dar çubuk) sahipse, bu saatlerin çok tutarlı olduğu demektir. Geceleri ise geniş çubuk görülebilir çünkü bazı günlerde çok az yolcu, bazı günlerde daha fazla yolcu olabilir.

---

### 11. GÜN-SAT İLİŞKİSİ

**Grafik 14 (Heatmap - Gün x Saat):**

Bu çok önemli bir grafiktir. Her gün ve saat kombinasyonunun ne kadar yoğun olduğunu göstermektedir.

- **Kırmızı (yüksek)**: O gün o saatte çok yolcu
- **Sarı (orta)**: Orta yoğunluk
- **Yeşil (düşük)**: Az yolcu

Grafik çizgi çizgi incelenebilir:
- **Pazartesi vs Cuma arası**: Hangi gün daha yoğun?
- **Cumartesi-Pazar**: Hafta içinden nasıl farklı?

Bu grafik, haftalık planlama ve taşıma kapasitesi planlaması için kullanılabilir.

---

## Sonuç ve Değerlendirmeler

### Güçlü Yönler
✓ **Geniş ağ**: Otobüs, metro, tramvay, vapur ile entegre sistem  
✓ **Direkt rotalar**: %89 kullanıcı aktarma yapmadan ulaşabiliyor  
✓ **Sosyal entegrasyon**: İndirimli biletler ile herkese ulaşılıyor  
✓ **Veri kayıt sistemi**: Saatlik detaylı veri toplamak önemli bir altyapı  

### İyileştirme Alanları
⚠ **Gece taşımacılığı**: Gece saatleri çok zayıf hizmet  
⚠ **Bakırköy'e aşırı bağımlılık**: Kuzey-Güney dengesizliği  
⚠ **Aktarma noktaları**: %10.9 aktarma oranı yüksek olabilir, aşağı çekilebilir  
⚠ **Veri kalitesi**: Ayın sonu verisindeki düşüş incelenmeli  

### İleriye Dönük Öneriler

1. **Gece servisleri**: Geceleri daha sık otobüs seferri açılabilir
2. **Raylı sistem genişletme**: İç Anadolu bölgesine metro uzantısı
3. **Transfer merkezleri**: Ana istasyonlarda rahat ve hızlı transferler
4. **Dinamik fiyatlandırma**: Yoğun saatlerde indirim, boş saatlerde normalyolculandırma teşviki
5. **Veri paylaşımı**: Gerçek zamanlı taşıma bilgisi halka açılabilir

---

## Teknik Bilgiler

- **Programlama Dili**: Python
- **Kullanılan Kütüphaneler**: Pandas, Matplotlib, Seaborn, NumPy
- **Veri İşleme**: Veri temizlemesi, pivot table, groupby işlemleri
- **Görsellendirme**: 15 farklı grafik (line, bar, pie, heatmap, errorbar)
- **Çıktı Formatı**: PNG (yüksek çözünürlük - 300 DPI)

---

**Proje Sahibi**: YBS Öğrencisi  
**Tarih**: Ocak 2026  
**Veri Kaynak**: İstanbul Açık Veri Portalı
