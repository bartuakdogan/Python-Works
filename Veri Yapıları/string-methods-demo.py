website = "http://www.sadikturan.com"
kursAdi = "Python Dersleri: Sıfırdan İleri Seviye Python Programlama."

# 1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
sonuc = 'Hello World'.strip()
sonuc = 'Hello World'.lstrip()
sonuc = 'Hello World'.rstrip()
print(sonuc)


# 2- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.
sonuc = 'www.sadikturan.com'.strip('w.com')
print(sonuc)
# 3- 'kursAdi' karakter dizisinin tüm karakterlerini küçük harf yapın.
sonuc = kursAdi.lower()
print(sonuc)


# 4- 'website' içinde kaç tane a karakteri vardır ? (count('a'))
sonuc = website.count('a')
print(sonuc)
# 5- 'website' "www" ile başlayıp com ile bitiyor mu?
sonuc = website.startswith('www')
print(sonuc)

sonuc = website.endswith('com')
print(sonuc)

# 6- 'website' içinde '.com' ifadesi var mı?
sonuc = website.find('.com')
print(sonuc)


# 7- 'kursAdi' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
sonuc = kursAdi.isalpha()
print(sonuc)

# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
sonuc = 'Contents'.center(50,'*')
sonuc = 'Contents'.ljust(50,'*')
sonuc = 'Contents'.rjust(50,'*')


# 9- 'kursAdi' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
sonuc = kursAdi.replace(' ','-')
print(sonuc)


# 10-'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin
msg = 'Hello World'
sonuc = msg.replace('World','There')
print(sonuc)


# 11-'kursAdi' karakter dizisini boşluk karakterlerinden ayırın.
sonuc = kursAdi.split()
print(sonuc)