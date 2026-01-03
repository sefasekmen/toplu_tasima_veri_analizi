import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

dosya_ismi = '4546fb79-e598-4dc7-888b-626361110e37.csv'

print(f"{dosya_ismi} yükleniyor...")

try:
    df = pd.read_csv(dosya_ismi)
    print(f"Veri yüklendi: {len(df):,} satır\n")
    
    if len(df) == 0:
        print("Hata: CSV dosyası boş!")
        exit()
        
except FileNotFoundError:
    print(f"Hata: '{dosya_ismi}' dosyası bulunamadı!")
    exit()

df['transition_date'] = pd.to_datetime(df['transition_date'])
df['Gun_Ismi'] = df['transition_date'].dt.day_name()

gunler_cevirme = {
    'Monday': 'Pazartesi', 'Tuesday': 'Salı', 'Wednesday': 'Çarşamba', 
    'Thursday': 'Perşembe', 'Friday': 'Cuma', 'Saturday': 'Cumartesi', 'Sunday': 'Pazar'
}
df['Gun_Ismi'] = df['Gun_Ismi'].map(gunler_cevirme)
df['Hafta_Turu'] = df['Gun_Ismi'].apply(lambda x: 'Hafta İçi' if x not in ['Cumartesi', 'Pazar'] else 'Hafta Sonu')

print("="*70)
print("İSTANBUL TOPLU TAŞIMA VERİ ANALİZİ - EYLÜL 2024")
print("="*70)

print("\n[GENEL BİLGİLER]")
print(f"Toplam yolcu sayısı: {df['number_of_passenger'].sum():,}")
print(f"Toplam veri noktası: {len(df):,}")
print(f"Tarih aralığı: {df['transition_date'].min().date()} ile {df['transition_date'].max().date()}")
print(f"Günlük ortalama yolcu: {df.groupby('transition_date')['number_of_passenger'].sum().mean():,.0f}")

saatlik_yogunluk = df.groupby('transition_hour')['number_of_passenger'].sum().reset_index()
saatlik_ort = df.groupby('transition_hour')['number_of_passenger'].mean().reset_index()

print("\n[SAATLIK TRAFİK ANALİZİ]")
en_yogun_saat = saatlik_yogunluk.loc[saatlik_yogunluk['number_of_passenger'].idxmax()]
en_az_yogun = saatlik_yogunluk.loc[saatlik_yogunluk['number_of_passenger'].idxmin()]
print(f"En yoğun saat: {int(en_yogun_saat['transition_hour']):02d}:00 ({int(en_yogun_saat['number_of_passenger']):,} yolcu)")
print(f"En az yoğun saat: {int(en_az_yogun['transition_hour']):02d}:00 ({int(en_az_yogun['number_of_passenger']):,} yolcu)")
print(f"Trafik farkı: {int(en_yogun_saat['number_of_passenger'] / en_az_yogun['number_of_passenger']):.0f}x")

zirve_limit = saatlik_yogunluk['number_of_passenger'].mean() * 1.25
zirve_saatler = saatlik_yogunluk[saatlik_yogunluk['number_of_passenger'] > zirve_limit]['transition_hour'].tolist()
print(f"Yoğun saatler: {[int(s) for s in zirve_saatler]}")

gun_sirasi = ['Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma', 'Cumartesi', 'Pazar']
gunluk = df.groupby('Gun_Ismi')['number_of_passenger'].sum().reindex(gun_sirasi).reset_index()
gunluk.columns = ['Gun_Ismi', 'number_of_passenger']

print("\n[GÜNLÜK ANALİZ]")
en_yogun_gun = gunluk.loc[gunluk['number_of_passenger'].idxmax()]
en_az_gun = gunluk.loc[gunluk['number_of_passenger'].idxmin()]
print(f"En yoğun gün: {en_yogun_gun['Gun_Ismi']} ({int(en_yogun_gun['number_of_passenger']):,} yolcu)")
print(f"En az yoğun gün: {en_az_gun['Gun_Ismi']} ({int(en_az_gun['number_of_passenger']):,} yolcu)")

hafta_iceği = df[df['Hafta_Turu'] == 'Hafta İçi']['number_of_passenger'].mean()
hafta_sonu = df[df['Hafta_Turu'] == 'Hafta Sonu']['number_of_passenger'].mean()
fark_yuzde = ((hafta_sonu - hafta_iceği) / hafta_iceği * 100)
print(f"Hafta içi ort: {hafta_iceği:,.0f} yolcu/saat")
print(f"Hafta sonu ort: {hafta_sonu:,.0f} yolcu/saat")
print(f"Fark: {fark_yuzde:+.1f}%")

tur = df.groupby('road_type')['number_of_passenger'].sum().reset_index().sort_values('number_of_passenger', ascending=False)

print("\n[TAŞIMACILIM TÜRÜ]")
toplam = tur['number_of_passenger'].sum()
for idx, row in tur.iterrows():
    yuzde = (row['number_of_passenger'] / toplam) * 100
    print(f"  {row['road_type']:12s}: {int(row['number_of_passenger']):>10,} ({yuzde:5.1f}%)")

tur_saatlik = df.pivot_table(index='transition_hour', columns='road_type', values='number_of_passenger', aggfunc='sum')

urun = df.groupby('product_kind')['number_of_passenger'].sum().reset_index().sort_values('number_of_passenger', ascending=False)

print("\n[BİLET TÜRÜ]")
for idx, row in urun.head(5).iterrows():
    yuzde = (row['number_of_passenger'] / toplam) * 100
    print(f"  {str(row['product_kind'])[:15]:15s}: {int(row['number_of_passenger']):>10,} ({yuzde:5.1f}%)")

ilce = df.groupby('town')['number_of_passenger'].sum().reset_index().sort_values('number_of_passenger', ascending=False)

print("\n[İLÇE ANALİZİ - TOP 5]")
for idx, row in ilce.head(5).iterrows():
    yuzde = (row['number_of_passenger'] / toplam) * 100
    print(f"  {str(row['town'])[:15]:15s}: {int(row['number_of_passenger']):>10,} ({yuzde:5.1f}%)")

hat = df.groupby('line_name')['number_of_passenger'].sum().reset_index().sort_values('number_of_passenger', ascending=False)

print("\n[EN YOĞUN HATLAR - TOP 5]")
for idx, row in hat.head(5).iterrows():
    print(f"  {str(row['line_name'])[:25]:25s}: {int(row['number_of_passenger']):>10,}")

transfer = df.groupby('transfer_type')['number_of_passenger'].sum().reset_index().sort_values('number_of_passenger', ascending=False)

print("\n[TRANSFER TÜRÜ]")
for idx, row in transfer.iterrows():
    yuzde = (row['number_of_passenger'] / toplam) * 100
    print(f"  {str(row['transfer_type'])[:12]:12s}: {int(row['number_of_passenger']):>10,} ({yuzde:5.1f}%)")

islem = df.groupby('transaction_type_desc')['number_of_passenger'].sum().reset_index().sort_values('number_of_passenger', ascending=False)

print("\n[İŞLEM TÜRÜ - TOP 5]")
for idx, row in islem.head(5).iterrows():
    yuzde = (row['number_of_passenger'] / toplam) * 100
    print(f"  {str(row['transaction_type_desc'])[:20]:20s}: {int(row['number_of_passenger']):>10,} ({yuzde:5.1f}%)")

gunluk_toplam = df.groupby('transition_date')['number_of_passenger'].sum().reset_index()
print("\n[AYLIK TREND]")
print(f"1. gün: {int(gunluk_toplam.iloc[0]['number_of_passenger']):,} yolcu")
print(f"Son gün: {int(gunluk_toplam.iloc[-1]['number_of_passenger']):,} yolcu")
trend = ((gunluk_toplam.iloc[-1]['number_of_passenger'] - gunluk_toplam.iloc[0]['number_of_passenger']) / gunluk_toplam.iloc[0]['number_of_passenger'] * 100)
print(f"Değişim: {trend:+.1f}%")

print("\n[GRAFİKLER OLUŞTURULUYOR...]")

import os
os.makedirs('grafik_analizi', exist_ok=True)

sns.set_theme(style="whitegrid")
fig = plt.figure(figsize=(20, 24))

ax1 = plt.subplot(5, 3, 1)
sns.lineplot(data=saatlik_yogunluk, x='transition_hour', y='number_of_passenger', 
             marker='o', color='#2E86AB', linewidth=2.5, ax=ax1)
ax1.fill_between(saatlik_yogunluk['transition_hour'], saatlik_yogunluk['number_of_passenger'], alpha=0.3, color='#2E86AB')
ax1.set_title('Saatlik Yolcu Trafikı', fontsize=12, fontweight='bold')
ax1.set_xlabel('Saat')
ax1.set_ylabel('Yolcu sayısı')
ax1.set_xticks(range(0, 24, 2))
ax1.grid(True, linestyle='--', alpha=0.5)

ax2 = plt.subplot(5, 3, 2)
renkler_gun = ['#FF6B6B' if g in ['Cumartesi', 'Pazar'] else '#4ECDC4' for g in gun_sirasi]
sns.barplot(data=gunluk, x='Gun_Ismi', y='number_of_passenger', palette=renkler_gun, ax=ax2)
ax2.set_title('Günlük Yolcu Dağılımı', fontsize=12, fontweight='bold')
ax2.set_xlabel('')
ax2.set_ylabel('Yolcu sayısı')
ax2.tick_params(axis='x', rotation=45)
for i, v in enumerate(gunluk['number_of_passenger']):
    ax2.text(i, v + 100000, f'{int(v/1e6):.2f}M', ha='center', va='bottom', fontsize=9)

ax3 = plt.subplot(5, 3, 3)
renkler = plt.cm.Set3(np.linspace(0, 1, len(tur)))
wedges, texts, autotexts = ax3.pie(tur['number_of_passenger'], 
                                     labels=tur['road_type'],
                                     autopct='%1.1f%%',
                                     colors=renkler,
                                     startangle=90)
ax3.set_title('Taşımacılık Türü Pazar Payı', fontsize=12, fontweight='bold')
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')

ax4 = plt.subplot(5, 3, 4)
pivot_tur = df.pivot_table(index='road_type', columns='transition_hour', values='number_of_passenger', aggfunc='sum')
sns.heatmap(pivot_tur, cmap='YlOrRd', cbar_kws={'label': 'Yolcu'}, ax=ax4, fmt='.0f')
ax4.set_title('Taşımacılık Türü x Saat Haritası', fontsize=12, fontweight='bold')
ax4.set_xlabel('Saat')
ax4.set_ylabel('Taşımacılık türü')

ax5 = plt.subplot(5, 3, 5)
hafta_data = df.groupby('Hafta_Turu')['number_of_passenger'].sum().reset_index()
sns.barplot(data=hafta_data, x='Hafta_Turu', y='number_of_passenger', palette=['#4ECDC4', '#FF6B6B'], ax=ax5)
ax5.set_title('Hafta İçi vs Hafta Sonu', fontsize=12, fontweight='bold')
ax5.set_xlabel('')
ax5.set_ylabel('Yolcu sayısı')
for i, v in enumerate(hafta_data['number_of_passenger']):
    ax5.text(i, v + 200000, f'{int(v/1e6):.1f}M', ha='center', va='bottom', fontsize=10, fontweight='bold')

ax6 = plt.subplot(5, 3, 6)
sns.barplot(data=ilce.head(10), x='number_of_passenger', y='town', palette='viridis', ax=ax6)
ax6.set_title('En Yoğun 10 İlçe', fontsize=12, fontweight='bold')
ax6.set_xlabel('Yolcu sayısı')
ax6.set_ylabel('')

ax7 = plt.subplot(5, 3, 7)
sns.barplot(data=hat.head(10), x='number_of_passenger', y='line_name', palette='cool', ax=ax7)
ax7.set_title('En Yoğun 10 Hat', fontsize=12, fontweight='bold')
ax7.set_xlabel('Yolcu sayısı')
ax7.set_ylabel('')

ax8 = plt.subplot(5, 3, 8)
sns.barplot(data=urun.head(8), x='number_of_passenger', y='product_kind', palette='magma', ax=ax8)
ax8.set_title('Bilet Türü Dağılımı', fontsize=12, fontweight='bold')
ax8.set_xlabel('Yolcu sayısı')
ax8.set_ylabel('')

ax9 = plt.subplot(5, 3, 9)
renkler_transfer = plt.cm.Set2(np.linspace(0, 1, len(transfer)))
wedges, texts, autotexts = ax9.pie(transfer['number_of_passenger'], 
                                     labels=transfer['transfer_type'],
                                     autopct='%1.1f%%',
                                     colors=renkler_transfer)
ax9.set_title('Transfer Türü Dağılımı', fontsize=12, fontweight='bold')
for autotext in autotexts:
    autotext.set_fontweight('bold')

ax10 = plt.subplot(5, 3, 10)
sns.lineplot(data=gunluk_toplam, x='transition_date', y='number_of_passenger', color='#C73E1D', linewidth=2.5, ax=ax10)
ax10.fill_between(gunluk_toplam['transition_date'], gunluk_toplam['number_of_passenger'], alpha=0.3, color='#C73E1D')
ax10.set_title('Günlük Trend', fontsize=12, fontweight='bold')
ax10.set_xlabel('Tarih')
ax10.set_ylabel('Yolcu sayısı')
ax10.tick_params(axis='x', rotation=45)
ax10.grid(True, linestyle='--', alpha=0.5)

ax11 = plt.subplot(5, 3, 11)
if not tur_saatlik.empty:
    tur_saatlik.plot(kind='bar', stacked=True, ax=ax11, colormap='tab10')
    ax11.set_title('Saatlik Taşımacılık Dağılımı', fontsize=12, fontweight='bold')
    ax11.set_xlabel('Saat')
    ax11.set_ylabel('Yolcu sayısı')
    ax11.legend(title='Taşımacılık', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8)
    ax11.tick_params(axis='x', rotation=45)

ax12 = plt.subplot(5, 3, 12)
sns.barplot(data=islem.head(8), x='number_of_passenger', y='transaction_type_desc', palette='husl', ax=ax12)
ax12.set_title('İşlem Türü', fontsize=12, fontweight='bold')
ax12.set_xlabel('Yolcu sayısı')
ax12.set_ylabel('')

ax13 = plt.subplot(5, 3, 13)
sns.lineplot(data=saatlik_ort, x='transition_hour', y='number_of_passenger', 
             marker='s', color='#B5651D', linewidth=2, ax=ax13)
ax13.set_title('Saatlik Ort. Yolcu (Gün başına)', fontsize=12, fontweight='bold')
ax13.set_xlabel('Saat')
ax13.set_ylabel('Ort. yolcu')
ax13.set_xticks(range(0, 24, 2))
ax13.grid(True, linestyle='--', alpha=0.5)

ax14 = plt.subplot(5, 3, 14)
gun_saat = df.pivot_table(index='Gun_Ismi', columns='transition_hour', values='number_of_passenger', aggfunc='sum')
gun_saat = gun_saat.reindex(gun_sirasi)
sns.heatmap(gun_saat, cmap='RdYlGn_r', cbar_kws={'label': 'Yolcu'}, ax=ax14, fmt='.0f')
ax14.set_title('Gün x Saat Yoğunluk Haritası', fontsize=12, fontweight='bold')
ax14.set_xlabel('Saat')
ax14.set_ylabel('Gün')

ax15 = plt.subplot(5, 3, 15)
saat_istatistik = df.groupby('transition_hour')['number_of_passenger'].agg(['mean', 'std']).reset_index()
ax15.errorbar(saat_istatistik['transition_hour'], saat_istatistik['mean'], 
              yerr=saat_istatistik['std'], fmt='o-', capsize=5, capthick=2, color='#1A535C', linewidth=2, markersize=6)
ax15.fill_between(saat_istatistik['transition_hour'], 
                   saat_istatistik['mean'] - saat_istatistik['std'],
                   saat_istatistik['mean'] + saat_istatistik['std'],
                   alpha=0.2, color='#1A535C')
ax15.set_title('Saatlik Trafik - Ortalama ± Std Sapma', fontsize=12, fontweight='bold')
ax15.set_xlabel('Saat')
ax15.set_ylabel('Ort. yolcu')
ax15.set_xticks(range(0, 24, 2))
ax15.grid(True, linestyle='--', alpha=0.5)

plt.suptitle('İSTANBUL TOPLU TAŞIMA ANALİZİ - EYLÜL 2024', fontsize=16, fontweight='bold', y=0.995)
plt.tight_layout()
plt.savefig('grafik_analizi.png', dpi=300, bbox_inches='tight')
print("Toplu grafik kaydedildi: grafik_analizi.png")

print("Bireysel grafikler kaydediliyor...")

fig1 = plt.figure(figsize=(12, 6))
sns.lineplot(data=saatlik_yogunluk, x='transition_hour', y='number_of_passenger', 
             marker='o', color='#2E86AB', linewidth=2.5)
plt.fill_between(saatlik_yogunluk['transition_hour'], saatlik_yogunluk['number_of_passenger'], alpha=0.3, color='#2E86AB')
plt.title('Saatlik Yolcu Trafikı', fontsize=14, fontweight='bold')
plt.xlabel('Saat')
plt.ylabel('Yolcu sayısı')
plt.xticks(range(0, 24, 2))
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('grafik_analizi/1_saatlik_yolcu_trafigi.png', dpi=300, bbox_inches='tight')
plt.close()

fig2 = plt.figure(figsize=(12, 6))
renkler_gun = ['#FF6B6B' if g in ['Cumartesi', 'Pazar'] else '#4ECDC4' for g in gun_sirasi]
sns.barplot(data=gunluk, x='Gun_Ismi', y='number_of_passenger', palette=renkler_gun)
plt.title('Günlük Yolcu Dağılımı', fontsize=14, fontweight='bold')
plt.xlabel('')
plt.ylabel('Yolcu sayısı')
plt.xticks(rotation=45)
for i, v in enumerate(gunluk['number_of_passenger']):
    plt.text(i, v + 100000, f'{int(v/1e6):.2f}M', ha='center', va='bottom', fontsize=9)
plt.tight_layout()
plt.savefig('grafik_analizi/2_gunluk_dagilimi.png', dpi=300, bbox_inches='tight')
plt.close()

fig3 = plt.figure(figsize=(10, 8))
renkler = plt.cm.Set3(np.linspace(0, 1, len(tur)))
plt.pie(tur['number_of_passenger'], labels=tur['road_type'], autopct='%1.1f%%', colors=renkler, startangle=90)
plt.title('Taşımacılık Türü Pazar Payı', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('grafik_analizi/3_tasimacilim_turu_pazar.png', dpi=300, bbox_inches='tight')
plt.close()

fig4 = plt.figure(figsize=(12, 8))
pivot_tur = df.pivot_table(index='road_type', columns='transition_hour', values='number_of_passenger', aggfunc='sum')
sns.heatmap(pivot_tur, cmap='YlOrRd', cbar_kws={'label': 'Yolcu'}, fmt='.0f')
plt.title('Taşımacılık Türü x Saat Haritası', fontsize=14, fontweight='bold')
plt.xlabel('Saat')
plt.ylabel('Taşımacılık türü')
plt.tight_layout()
plt.savefig('grafik_analizi/4_tasimacilim_saat_haritasi.png', dpi=300, bbox_inches='tight')
plt.close()

fig5 = plt.figure(figsize=(10, 6))
hafta_data = df.groupby('Hafta_Turu')['number_of_passenger'].sum().reset_index()
sns.barplot(data=hafta_data, x='Hafta_Turu', y='number_of_passenger', palette=['#4ECDC4', '#FF6B6B'])
plt.title('Hafta İçi vs Hafta Sonu', fontsize=14, fontweight='bold')
plt.xlabel('')
plt.ylabel('Yolcu sayısı')
for i, v in enumerate(hafta_data['number_of_passenger']):
    plt.text(i, v + 200000, f'{int(v/1e6):.1f}M', ha='center', va='bottom', fontsize=11, fontweight='bold')
plt.tight_layout()
plt.savefig('grafik_analizi/5_hafta_karsilastirma.png', dpi=300, bbox_inches='tight')
plt.close()

fig6 = plt.figure(figsize=(12, 8))
sns.barplot(data=ilce.head(10), x='number_of_passenger', y='town', palette='viridis')
plt.title('En Yoğun 10 İlçe', fontsize=14, fontweight='bold')
plt.xlabel('Yolcu sayısı')
plt.ylabel('')
plt.tight_layout()
plt.savefig('grafik_analizi/6_top10_ilce.png', dpi=300, bbox_inches='tight')
plt.close()

fig7 = plt.figure(figsize=(12, 8))
sns.barplot(data=hat.head(10), x='number_of_passenger', y='line_name', palette='cool')
plt.title('En Yoğun 10 Hat', fontsize=14, fontweight='bold')
plt.xlabel('Yolcu sayısı')
plt.ylabel('')
plt.tight_layout()
plt.savefig('grafik_analizi/7_top10_hat.png', dpi=300, bbox_inches='tight')
plt.close()

fig8 = plt.figure(figsize=(12, 8))
sns.barplot(data=urun.head(8), x='number_of_passenger', y='product_kind', palette='magma')
plt.title('Bilet Türü Dağılımı', fontsize=14, fontweight='bold')
plt.xlabel('Yolcu sayısı')
plt.ylabel('')
plt.tight_layout()
plt.savefig('grafik_analizi/8_bilet_turu.png', dpi=300, bbox_inches='tight')
plt.close()

fig9 = plt.figure(figsize=(10, 8))
renkler_transfer = plt.cm.Set2(np.linspace(0, 1, len(transfer)))
plt.pie(transfer['number_of_passenger'], labels=transfer['transfer_type'], autopct='%1.1f%%', colors=renkler_transfer)
plt.title('Transfer Türü Dağılımı', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('grafik_analizi/9_transfer_turu.png', dpi=300, bbox_inches='tight')
plt.close()

fig10 = plt.figure(figsize=(12, 6))
sns.lineplot(data=gunluk_toplam, x='transition_date', y='number_of_passenger', color='#C73E1D', linewidth=2.5)
plt.fill_between(gunluk_toplam['transition_date'], gunluk_toplam['number_of_passenger'], alpha=0.3, color='#C73E1D')
plt.title('Günlük Trend', fontsize=14, fontweight='bold')
plt.xlabel('Tarih')
plt.ylabel('Yolcu sayısı')
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('grafik_analizi/10_gunluk_trend.png', dpi=300, bbox_inches='tight')
plt.close()

fig11 = plt.figure(figsize=(14, 8))
if not tur_saatlik.empty:
    tur_saatlik.plot(kind='bar', stacked=True, colormap='tab10')
    plt.title('Saatlik Taşımacılık Dağılımı (Yığılmış)', fontsize=14, fontweight='bold')
    plt.xlabel('Saat')
    plt.ylabel('Yolcu sayısı')
    plt.legend(title='Taşımacılık', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=9)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('grafik_analizi/11_saatlik_tasimacilim_dagilimi.png', dpi=300, bbox_inches='tight')
plt.close()

fig12 = plt.figure(figsize=(12, 8))
sns.barplot(data=islem.head(8), x='number_of_passenger', y='transaction_type_desc', palette='husl')
plt.title('İşlem Türü Dağılımı', fontsize=14, fontweight='bold')
plt.xlabel('Yolcu sayısı')
plt.ylabel('')
plt.tight_layout()
plt.savefig('grafik_analizi/12_islem_turu.png', dpi=300, bbox_inches='tight')
plt.close()

fig13 = plt.figure(figsize=(12, 6))
sns.lineplot(data=saatlik_ort, x='transition_hour', y='number_of_passenger', 
             marker='s', color='#B5651D', linewidth=2)
plt.title('Saatlik Ortalama Yolcu (Gün Başına)', fontsize=14, fontweight='bold')
plt.xlabel('Saat')
plt.ylabel('Ortalama yolcu')
plt.xticks(range(0, 24, 2))
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('grafik_analizi/13_saatlik_ortalama.png', dpi=300, bbox_inches='tight')
plt.close()

fig14 = plt.figure(figsize=(14, 8))
gun_saat = df.pivot_table(index='Gun_Ismi', columns='transition_hour', values='number_of_passenger', aggfunc='sum')
gun_saat = gun_saat.reindex(gun_sirasi)
sns.heatmap(gun_saat, cmap='RdYlGn_r', cbar_kws={'label': 'Yolcu'}, fmt='.0f')
plt.title('Gün x Saat Yoğunluk Haritası', fontsize=14, fontweight='bold')
plt.xlabel('Saat')
plt.ylabel('Gün')
plt.tight_layout()
plt.savefig('grafik_analizi/14_gun_saat_haritasi.png', dpi=300, bbox_inches='tight')
plt.close()

fig15 = plt.figure(figsize=(12, 6))
saat_istatistik = df.groupby('transition_hour')['number_of_passenger'].agg(['mean', 'std']).reset_index()
plt.errorbar(saat_istatistik['transition_hour'], saat_istatistik['mean'], 
             yerr=saat_istatistik['std'], fmt='o-', capsize=5, capthick=2, color='#1A535C', linewidth=2, markersize=6)
plt.fill_between(saat_istatistik['transition_hour'], 
                  saat_istatistik['mean'] - saat_istatistik['std'],
                  saat_istatistik['mean'] + saat_istatistik['std'],
                  alpha=0.2, color='#1A535C')
plt.title('Saatlik Trafik - Ortalama ± Std Sapma', fontsize=14, fontweight='bold')
plt.xlabel('Saat')
plt.ylabel('Ortalama yolcu')
plt.xticks(range(0, 24, 2))
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('grafik_analizi/15_standart_sapma.png', dpi=300, bbox_inches='tight')
plt.close()

print("Bireysel grafikler kaydedildi: grafik_analizi/ klasörü")
