#key--->value

plakalar = {'İstanbul':34,'Zonguldak':67}


plakalar['Ankara'] = 6

plakalar['İzmir'] = 35
plakalar['Kocaeli'] = 41



#print(plakalar)

#ogrenciler = {100:"Bartu","Berke":95,"Sercan":90}

#print(ogrenciler[100]) # kim 100 aldı sorusunun cevabını verir.

ogrenciler = {
    100: {
        'İsim':'Bartu',
        'Soyad':'Akdoğan',
        'Yaş':20,
        'Notlar': [85,90,94]
    },
    95:{
        'İsim':'Berke',
        'Soyad':'Yıldırım',
        'Yaş':20,
        'Notlar': [80,96,94]
    
    },

}

sonuc = (ogrenciler[100]['Notlar'][0] + ogrenciler[100]['Notlar'][1] + ogrenciler[100]['Notlar'][2]) / 3

print(sonuc)
  
