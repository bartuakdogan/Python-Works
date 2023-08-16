#isim = "Bartu Akdoğan"

#for harf in isim:
#    if (harf == 't'):
#        continue
#    print(harf)   # t harfini atlayıp sonraki tura geçer.

#for harf in isim:
#    if (harf == 't'):
#        break   
#    print(harf)  # t harfine geldiğinde döngüyü durdurur.

#i = 0
#while (i < 5):
#    if (i == 3):
#        break
#    print(i)
#    i += 1
#print("Döngü bitti.")       

# 1-100 arasındaki çift sayılar toplamı?

i = 0
toplam = 0

while (i<=100):
    i += 1
    if (i%2==1):
        continue
    toplam += i

print(f"toplam: {toplam}")    


 