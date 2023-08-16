# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz. 
# Ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır. 

ad = input("Adınız: ")
yas = int(input("Yaşınız: "))
egitimDurumu = input("Eğitim Durumunuz: ")

if (yas >= 18):
    if (egitimDurumu == "Lise") or (egitimDurumu == "Üniversite"):
        print("Ehliyet alabilirsiniz.")
    else:
        print("Ehliyet alamazsınız,çünkü eğitim durumunuz uygun değil.")
else:
    print("Ehliyet alamazsınız,çünkü yaşınız uygun değil.")            


# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık 
# gelen not bilgisini yazdırınız.
#    0 -24  => 0
#    25-44  => 1
#    45-54  => 2
#    55-69  => 3
#    70-84  => 4
#    85-100 => 5

yazili_1 = float(input("1. yazılınız: "))
yazili_2 = float(input("2. yazılınız: "))
sozlu = float(input("Sözlü notunuz: "))

ortalama = ((yazili_1 + yazili_2 + sozlu) / 3)

if (ortalama >= 0) and (ortalama < 25):
    print(f"Ortalamanız:{ortalama} Notunuz:0")
elif (ortalama >= 25) and (ortalama < 45):
    print(f"Ortalamanız:{ortalama} Notunuz:1")
elif (ortalama >= 45) and (ortalama < 55):
    print(f"Ortalamanız:{ortalama} Notunuz:2")
elif (ortalama >= 55) and (ortalama < 70):
    print(f"Ortalamanız:{ortalama} Notunuz:3")
elif (ortalama >= 70) and (ortalama < 85):
    print(f"Ortalamanız:{ortalama} Notunuz:4")
elif (ortalama >= 85) and (ortalama <=100):
    print(f"Ortalamanız:{ortalama} Notunuz:5")
else:
    print("Girdiğiniz bilgiler yanlış.")                    





# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız.
#    1. Bakım => 1. yıl     
#    2. Bakım => 2. yıl      
#    3. Bakım => 3. yıl     
#    ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız..
#    *** datetime modülünü kullanmanız gerekiyor.  
#    (simdi) - (2018/8/1) => gün

import datetime

tarih = input("Aracınız  hangi tarihte trafiğe çıktı? (2019/7/11)")
tarih = tarih.split("/")
#print(tarih[0],tarih[1],tarih[2])

simdi = datetime.datetime.now()
trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))

fark = simdi - trafigeCikis
gun = fark.days
print(gun)

if (gun <= 365):
    print("1. Servis Bakımı")
elif (gun > 365) and (gun <= 365 * 2):
    print("2. Servis Bakımı")
elif (gun > 365 * 2) and (gun <= 365 * 3):
    print("3. Servis Bakımı")
else:
    print("Girdiğiniz bilgiler yanlış.")    



