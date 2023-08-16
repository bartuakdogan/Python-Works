sayilar = [4,6,9,10,35,57,89,125,244]

# 1: sayilar listesini while ile ekrana yazdırın.

#i = 0
#while (i<len(sayilar)):
#    print(sayilar[i])
#   i += 1

# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları 
# ekrana yazdırın.

#baslangic = int(input("Başlangıç: "))
#bitis = int(input("Bitiş: "))

#i = baslangic

#while i<bitis:
#    i += 1
#    if (i % 2 == 1):
#        print(i)


# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.

#i = 100
#while i > 0:
#   print(i)
#    i-=1

# 4: Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.

sayilar = []

i = 0
while i<5:
    sayi = int(input("Bir sayı giriniz: "))
    sayilar.append(sayi)
    i += 1

sayilar.sort()
print(sayilar)    