isimler = ['Ada','Yiğit','Hasan','Beril']
yaslar = [1998, 2000, 1998, 1987]

# 1-  "Cenk" ismini listenin sonuna ekleyiniz.
#isimler.append('Cenk')

#print(isimler)

# 2-  "Sena" değerini listenin başına ekleyiniz.

#isimler.insert(0,'Sena')

#print(isimler)


# 3-  "Yiğit" ismini listeden siliniz.

#isimler.remove('Yiğit')
#print(isimler)

# 4-  "Yiğit" isminin indeksi nedir ?

#print(isimler.index('Yiğit'))


# 5-  "Beril" listenin bir elemanı mıdır ?

#sonuc = 'Beril' in isimler

#print(sonuc)

# 6-  Liste elemanlarını ters çevirin.

#isimler.reverse()
#yaslar.reverse()

#print(isimler)
#print(yaslar)

# 7-  Liste elemanlarını alfabetik olarak sıralayınız.

#isimler.sort()

#print(isimler)

# 8-  yaslar listesini rakamsal büyüklüğe göre sıralayınız.

#yaslar.sort()

#print(yaslar)

# 9-  s = "IPhone X,IPhone XR" karakter dizisini listeye çeviriniz.

#s = 'Iphone X,Iphone XR'
#sonuc = s.split(',')

#print(sonuc)

# 10- yaslar dizisinin en büyük ve en küçük elemanı nedir ?

#print(min(yaslar))

#print(max(yaslar))


# 11- yaslar dizisinde kaç tane 1998 değeri vardır ?

#print(yaslar.count(1998))


# 12- yaslar dizisinin tüm elemanlarını siliniz.

#print(yaslar.clear())

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.

markalar = []

marka = input("marka: ")
markalar.append(marka)


marka = input("marka: ")
markalar.append(marka)


marka = input("marka: ")
markalar.append(marka)

print(markalar)


