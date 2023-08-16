from datetime import datetime


def selamlama():
    print('Merhaba')

#selamlama()

#for i in range(11):
#    selamlama()

#a = 10
#b = 20 

#def topla():
#    print(a + b)

#topla()   

#def toplam():
#    return 10+20

#sonuc = toplam() + 50
#print(sonuc)

def yil():
    import datetime
    return datetime.datetime.now().year

def yasHesapla():
    return yil() - 1980

sonuc = yasHesapla()

def saat():
    import datetime
    return datetime.datetime.now().hour

def selamla():
    if (saat()<12):
        return "Günaydın!"
    elif (saat()>=12) and (saat()<18):
        return "Tünaydın!"
    elif (saat()>18) and (saat()<22):
        return "İyi Akşamlar!"
    elif (saat()>=22):
        return "İyi Geceler!"        

             

sonuc = selamla()
print(sonuc) 