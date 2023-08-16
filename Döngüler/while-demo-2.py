#    Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
#    ** ürün sayısını kullanıcıya sorun.
#    ** dictionary listesi yapısı (urunAdi, fiyat) şeklinde olsun.
#    ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.

i = 0
adet = int(input("Kaç adet ürün eklemek istiyorsunuz?: "))
urunler = []

while (i < adet):
    urunAdi = input("Ürün Adı: ")
    fiyat = input("Ürün Fiyatı: ")
    urunler.append({
        'Ürün Adı': urunAdi,
        'Ürün Fiyatı': fiyat
    })
    i +=1
print(urunler)    


a = 0
while (a<len(urunler)):
    print(f"Ürün Adı: {urunler[a]['Ürün Adı']} Ürün Fiyatı: {urunler[a]['Ürün Fiyatı']}")
    a += 1