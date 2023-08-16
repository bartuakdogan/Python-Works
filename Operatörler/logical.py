# yaş >= 18 ve  (mezuniyet == 'lise' ya da mezuniyet == 'üniversite')

from ast import And


x = 8

#1-And Operatörü (ve)
#sonuc = 5 < x < 15
sonuc = (x > 5) and (x < 15)

#True ve True => True
#True ve False => False
#False ve False => False

hak = 3
devam = 'e'

sonuc = (hak > 0) and (devam == 'e')

print(sonuc)

# 2- or operatörü(veya)

sonuc = (x > 0) or (x % 2 == 0) # veya dediği için(or) ikisinden biri doğruysa True cevabını alırız.
print(sonuc)

# 3- not operatörü(değildir)

sonuc = not (x > 0)  # x 0'dan büyük değil mi? cevap:False(hayır), büyük.
print(sonuc)

# x,5 ve 10 arasında bir çift sayı mıdır?

sonuc = ((x>5) and (x<10)) and (x % 2 == 0)
print(sonuc)