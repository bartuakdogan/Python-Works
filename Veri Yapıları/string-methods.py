msg = "Merhabalar.Benim adım Bartu."

#sonuc = msg.upper()--> tamamı büyük harf
#sonuc = msg.lower()--> tamamı küçük harf
#sonuc = msg.title()--> her kelimenin ilk harfi büyük
#sonuc = msg.capitalize() --> sadece ilk harf büyük
#sonuc = msg.islower()--> is:soru kalıbı   tüm harfleri küçük mü diye soruyoruz.
#sonuc = msg.isdigit()--> sayı var mı diye soruyoruz. yanıt False
#sonuc ="    abc   ".strip()-->.strip stringteki boşlukları ortadan kaldırır.
#sonuc = msg.split()--> .split cümleyi tek tek kelimelerine ayırır.
#sonuc = msg.split()
#sonuc = "-".join(sonuc)
# .strip() komutu boşlukları kaldırır.
#index = msg.index('adım')-->adım kelimesinin kaçıncı indexten(numaradan)başladğını gösterir.
#sonuc = msg.startswith('M')--> M ile mi başlıyor diye sorduk.True cevabını aldık.
#sonuc = msg.endswith('.')
sonuc = msg.replace('adım','Bartu')
sonuc = msg.replace(' ', '-').replace('Bartu','Melisa Ecrin')
print(sonuc)
