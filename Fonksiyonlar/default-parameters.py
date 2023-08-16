def selamlama(isim="Kullanıcı",mesaj="İyi Günler"):    # default olarak "Kullanıcı" ve "İyi Günler" atadık.
    print(f"{mesaj} {isim}")                           # Eğer hiçbir şey belirtmezsek default olarak bunlar yazdırılır.

selamlama("Ali","Günaydın")
selamlama("Ali","İyi Günler")
selamlama("Ali")
selamlama()

def usAlma(taban,us=2):      # us=2 atamasını yaptığımızda default olarak hangi tabanı yazarsak yazalım karesi
    return taban ** us       # karesi alınacak.

sonuc = usAlma(2,3)
sonuc = usAlma(3,3)
sonuc = usAlma(5)

def toplam(a,b):
    return a + b

def cikarma(a,b):
    return a - b

def islem(a,b,fn=toplam):                            # fn fonksiyon çağırmak için kullandık.
    return fn(a,b) 
    
sonuc = islem(5,3,cikarma)                      
sonuc = islem(6,4,toplam)


print(sonuc)    