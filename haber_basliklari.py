import requests
from bs4 import BeautifulSoup
import pandas as pd

# BBC News anasayfasının URL'si
url = "https://www.bbc.com/"

# HTTP isteği gönder
response = requests.get(url)

# Sayfa içeriğini BeautifulSoup ile parse et
soup = BeautifulSoup(response.text, 'html.parser')

# Başlıkları bul (h2 etiketlerini kontrol et)
headlines = soup.find_all('h2')

# Başlıkları temizleyip bir listeye aktar
headlines_list = [headline.get_text() for headline in headlines if headline.get_text() != ""]

# Başlıkları bir DataFrame'e dönüştür
df = pd.DataFrame(headlines_list, columns=["Başlık"])

# Başlıkları yazdır
print("\nBaşlıklar:")
print(df.head())

# Kelime sayısı hesaplama
df['Kelime Sayısı'] = df['Başlık'].apply(lambda x: len(x.split()))

# Başlıkların ve kelime sayılarının ilk 5 satırını yazdır
print("\nBaşlıkların Kelime Sayısı:")
print(df.head())

# Sonuçları CSV dosyasına kaydetme
df.to_csv("haber_basliklari_ve_kelime_sayisi.csv", index=False)
print("\nBaşlıklar ve Kelime Sayıları 'haber_basliklari_ve_kelime_sayisi.csv' dosyasına kaydedildi.")
