# Bankamatik Uygulaması

BartuHesap = {
    "ad": "Bartu Akdoğan",
    "hesapNo": "12345678",
    "bakiye": 3000,
    "ek hesap": 2000
}

MelisHesap = {
    "ad": "Melisa Ecrin Aldırmaz",
    "hesapNo": "13245678",
    "bakiye": 4000,
    "ek hesap": 3000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print("Paranızı alabilirsiniz.")
    else:
        toplam = hesap['bakiye'] + hesap['ek hesap']

        if (toplam >= miktar):
            ekHesapKullanimi = input("Ek hesap kullanılsın mı? (Evet/Hayır)")

            if ekHesapKullanimi == "Evet":
                print("Paranızı alabilirsiniz.")
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bakiye bulunmaktadır.") 

        else:
            print('Üzgünüz,bakiye yetersiz.')

paraCek(BartuHesap, 4000)        




