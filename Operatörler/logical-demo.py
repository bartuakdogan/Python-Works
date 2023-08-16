# 1- Girilen bir sayının 50-100 arasında olup olmadığını kontrol ediniz.
#sayi = int(input("Bir sayı giriniz: "))

#sonuc = (sayi > 50) and (sayi < 100)

#print(f"Girdiğiniz sayı bu değerler arasındadır: {sonuc}")

# 2- Girilen bir sayının pozitif tek sayı olup olmadığını kontrol ediniz.
#sayi = int(input("Bir sayı giriniz: "))

#sonuc = (sayi > 0) and (sayi % 2 == 1)

#print(f"Girilen sayı pozitif bir tek sayıdır:{sonuc}")

# 3- Username ve parola bilgileri ile giriş kontrolü yapınız. 
#_username = "bartuakdogan10"
#_password = "BartuMelis2002"

#username = input("Username: ")
#password = input("Password: ")

#sonuc = (username == _username) and (password == _password)
#print(f"Girdiğiniz username ve password bilgileri doğru,hesabınıza giriş yaptınız:{sonuc}")

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
#x = int(input("x: "))
#y = int(input("y: "))
#z = int(input("z: "))

#sonuc = (x>y) and (x>z) # x en büyük
#print(f"x,en büyüktür:{sonuc}")

#sonuc = (y>x) and (y>z) # y en büyük
#print(f"y,en büyüktür:{sonuc}")

#sonuc = (z>x) and (z>y) # z en büyük
#print(f"z,en büyüktür:{sonuc}")


# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#    a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
#    b-) Finalden 70 alındığında ortalamanın önemi olmasın.

#vize1 = float(input("Vize 1: "))
#vize2 = float(input("Vize 2: "))
#final = float(input("Final: "))

#ortalama = (((vize1 + vize2) / 2 * 0.6) + (final * 0.4))
#sonuc1 = (ortalama >= 50) and (final >= 50)
#sonuc = (final >= 70) or (ortalama >= 50)

#print(f"Öğrencinin not ortalaması: {ortalama} ve dersi geçme durumu: {sonuc}")

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

kiloIndeks = (kg / (hg ** 2))

zayif = (kiloIndeks >= 0) and (kiloIndeks <= 18.4)
normal = (kiloIndeks > 18.4) and (kiloIndeks <= 24.9)
fazlaKilolu = (kiloIndeks > 24.9) and (kiloIndeks <= 29.9)
obez = (kiloIndeks > 29.9) and (kiloIndeks <= 34.9)

print(f"{ad},Kilo İndeksin:{kiloIndeks} ve Kilo Değerlendirmen:Zayıf:{zayif}")

ad = input("Adınız: ")
kg = float(input("Kilonuz: "))
hg = float(input("Boyunuz: "))

kiloIndeks = (kg / (hg ** 2))

zayif = (kiloIndeks >= 0) and (kiloIndeks <= 18.4)
normal = (kiloIndeks > 18.4) and (kiloIndeks <= 24.9)
fazlaKilolu = (kiloIndeks > 24.9) and (kiloIndeks <= 29.9)
obez = (kiloIndeks > 29.9) and (kiloIndeks <= 34.9)

print(f"{ad},Kilo İndeksin:{kiloIndeks} ve Kilo Değerlendirmen:Normal:{normal}")

ad = input("Adınız: ")
kg = float(input("Kilonuz: "))
hg = float(input("Boyunuz: "))

kiloIndeks = (kg / (hg ** 2))

zayif = (kiloIndeks >= 0) and (kiloIndeks <= 18.4)
normal = (kiloIndeks > 18.4) and (kiloIndeks <= 24.9)
fazlaKilolu = (kiloIndeks > 24.9) and (kiloIndeks <= 29.9)
obez = (kiloIndeks > 29.9) and (kiloIndeks <= 34.9)

print(f"{ad},Kilo İndeksin:{kiloIndeks} ve Kilo Değerlendirmen:Fazla Kilolu:{fazlaKilolu}")

ad = input("Adınız: ")
kg = float(input("Kilonuz: "))
hg = float(input("Boyunuz: "))

kiloIndeks = (kg / (hg ** 2))

zayif = (kiloIndeks >= 0) and (kiloIndeks <= 18.4)
normal = (kiloIndeks > 18.4) and (kiloIndeks <= 24.9)
fazlaKilolu = (kiloIndeks > 24.9) and (kiloIndeks <= 29.9)
obez = (kiloIndeks > 29.9) and (kiloIndeks <= 34.9)

print(f"{ad},Kilo İndeksin:{kiloIndeks} ve Kilo Değerlendirmen:obez:{obez}")