# 1- Girilen 2 sayıdan hangisi büyüktür ?
#sayi1 = int(input('Sayı 1: '))
#sayi2 = int(input('Sayı 2: '))

#sonuc = (sayi1 > sayi2)

#print(f"{sayi1} , {sayi2} sayısından büyüktür: {sonuc}")

# 2- Girilen bir sayının tek mi çift mi olduğunu yazdırın.
#sayi = int(input('Bir sayı giriniz: '))

#sonuc = (sayi % 2 == 0)

#print(f"{sayi} sayısı bir çift sayıdır: {sonuc}")

# 3- Girilen bir sayının negatif pozitif durumunu yazdırın.
#sayi = int(input("Bir sayı giriniz: "))

#sonuc = (sayi > 0)

#print(f"{sayi},pozitif bir sayıdır: {sonuc}")

# 4- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.

#vize1 = float(input("Vize 1: "))
#vize2 = float(input("Vize 2: "))
#final = float(input("Final: "))

#ortalama = (((vize1 + vize2) / 2 * 0.6) + (final * 0.4))

#sonuc = (ortalama >= 50)

#print(f"Ortalamanız:{ortalama}.Dersi geçtiniz: {sonuc}")


# 5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
#    (email: info@sadikturan.com parola:12345)
_email = "info@sadikturan.com"
_password = "12345"

email = input("E-mail: ")
password = input("Password: ")

isEmail = (email.lower().strip() == _email)
isPassword = (password.strip() == _password)

print(f"E-mail doğruluğu:{isEmail} ve parola doğruluğu:{isPassword}")



