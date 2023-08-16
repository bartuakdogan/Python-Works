def selamla(isim):
    return "Merhaba," + isim

sonuc = selamla("Bartu")

def toplam(a,b):
    return a+b

sonuc = toplam(25,46)

def yasHesapla(dogumYili):
    return 2022 - dogumYili

sonuc = yasHesapla(1980)
sonuc = yasHesapla(2002)

#print(sonuc)

def emekliligeKacYilKaldi(dogumYili,isim):
    yas = yasHesapla(dogumYili)

    kalanSure = 65 - yas 

    if kalanSure > 0:
        print(f"{isim},emekliliğinize {kalanSure} yıl kaldı.")
    else:
        print(f"{isim},{abs(kalanSure)} yıl önce emekli oldunuz.")       #abs() mutlak değere alır!

emekliligeKacYilKaldi(1978,"Mustafa")        