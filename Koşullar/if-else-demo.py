# 1- Girilen bir sayının 50-100 arasında olup olmadığını kontrol ediniz.
sayi = int(input("Bir sayı giriniz: "))

if (sayi>50) and (sayi<100):
    print("Girdiğiniz sayı bu değerler arasındadır.")
else:
    print("Girdiğiniz sayı bu değerler arasında değildir.")    


# 2- Girilen bir sayının pozitif tek sayı olup olmadığını kontrol ediniz.
#sayi = int(input("Bir sayı giriniz."))

#if (sayi>0):
#    if (sayi % 2 == 1):
#        print("Girdiğiniz sayı pozitif bir tek sayıdır.")
#    else:
#        print("Girdiğiniz sayı pozitif ancak tek değil.")  
#else:
#    print("Girdiğiniz sayı negatif bir sayı.")          


# 3- Username ve parola bilgileri ile giriş kontrolü yapınız. 
#_Username = "bartuakdogan10"
#_Password = "BartuMelis2002"

#username = input("Username: ")
#password = input("Password: ")

#if (username.strip() == _Username) and (password.strip() == _Password):
#    print("Girilen bilgiler doğru,hesabınıza giriş yaptınız.")
#else:
#    print("Girdiğiniz bilgiler yanlış")    




# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
#x = int(input("x: "))
#y = int(input("y: "))
#z = int(input("z: "))

#if (x>y) and (x>z):
#    print("x,en büyük sayıdır.")
#elif (y>x) and (y>z):
#    print("y,en büyük sayıdır.")
#elif (z>x) and (z>y):
#    print("z,en büyük sayıdır.")        


# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    a-) Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#    b-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
#    c-) Finalden 70 alındığında ortalamanın önemi olmasın.

#vize1 = float(input("Vize 1: "))
#vize2 = float(input("Vize 2: "))
#final = float(input("Final: "))

#ortalama = (((vize1 + vize2) / 2 * 0.6) + (final * 0.4))

#durum1
#if (ortalama >= 50):
#    print(f"Ortalamanız:{ortalama} Dersi geçtiniz.")
#else:
#    print(f"Ortalamanız:{ortalama} Dersten kaldınız.")

#durum2
#if (ortalama >= 50):
#    if (final >= 50):
#        print(f"Ortalamanız:{ortalama} Dersi geçtiniz.")
#    else:
#        print(f"Ortalamanız:{ortalama} Dersten kaldınız.Final notunuz en az 50 olmalıdır.")
#else:
#    print(f"Ortalamanız:{ortalama} Dersten kaldınız.")  

#durum3
#if (ortalama >= 50):
#    print(f"Ortalamanız:{ortalama} Dersi geçtiniz.")
#else:
#    if (final >= 70):
#        print(f"Ortalamanız:{ortalama} Ancak final notunuz 70 ve üzeri olduğu için dersi geçtiniz.")
#    else:
#        print(f"Ortalamanız:{ortalama} Dersten kaldınız.")    
        
                            


# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formül: (Kilo / boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#    0-18.4    => Zayıf 
#    18.5-24.9 => Normal  
#    25.0-29.9 => Fazla Kilolu
#    30.0-34.9 => Şişman (Obez)

ad = input("Adınız: ")
kg = float(input("Kilonuz: "))
hg = float(input("Boyunuz: "))

kiloIndeks = kg / (hg ** 2)

zayif = (kiloIndeks >= 0) and (kiloIndeks <= 18.4)
normal = (kiloIndeks > 18.4) and (kiloIndeks <=24.9)
fazlaKilolu = (kiloIndeks > 24.9) and (kiloIndeks <= 29.9)
obez = (kiloIndeks > 29.9) and (kiloIndeks <= 34.9)

if (zayif):
    print(f"Adınız {ad},kilo indeksiniz:{kiloIndeks} ve kilo değerlendirmeniz:zayıf")
elif (normal):
    print(f"Adınız {ad},kilo indeksiniz:{kiloIndeks} ve kilo değerlendirmeniz:normal")
elif (fazlaKilolu):
    print(f"Adınız {ad},kilo indeksiniz:{kiloIndeks} ve kilo değerlendirmeniz:fazla kilolu")          
elif (obez):
    print(f"Adınız {ad},kilo indeksiniz:{kiloIndeks} ve kilo değerlendirmeniz:obez")
else:
    print("Bilgileriniz yanlış.")    