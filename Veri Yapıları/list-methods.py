sayilar = [1,5,8,9,3,45,3]
harfler = ['a','b','e','s','a','y']

sonuc = min(sayilar) # minimum sayı 1.
sonuc = max(sayilar) # maximum sayı 45.
sonuc = min(harfler) # min harf a.
sonuc = max(harfler) # max harf y.

#ekleme
sayilar.append(4) # .append komutu listenin sonuna parantez içine yazılanı ekler.
sayilar.insert(3,6) # .insert komutu (x,y) x-->kaçıncı indexe yerleşeceği;y-->hangi sayının ekleneceğini belirler.


#silme
sayilar.pop(3) # .pop listenin elemanını siler.
sayilar.remove(45) #.remove(45) '45' elemanını listeden çıkarır.
harfler.remove('a') # 'a' harfini listeden çıkardık.


#sıralama
sayilar.sort()
harfler.sort()
sayilar.reverse()#.reverse-->ters sıralama

sonuc = sayilar
#sonuc = harfler

print(sonuc)
# print(sayilar.count(3)) #.count dizi içinde bir elemandan kaç tane olduğunu bize gösterir.

print(sayilar.index(9)) # .index aradığımız elemanın kaçıncı index numarasında olduğunu gösterir.

