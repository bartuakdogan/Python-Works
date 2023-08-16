hyundaiObj = {
    "marka": "Hyundai",
    "model": "Tucson",
    "üretim yılı": 2021
}

sonuc = hyundaiObj["marka"]
sonuc = hyundaiObj.get('marka') # .get komutunun içine yazacağımız bilginin karşılığı gelir.

#for x in hyundaiObj:
#    print(x)

#for x in hyundaiObj:
#    print(hyundaiObj[x])    #bunu kullanmak yerine bir methodumuz var.(.values)


#for x in hyundaiObj.values(): # bu komutu kullanarak sadece value bilgilerini yazdırabiliriz.
#    print(x)


#for x,y in hyundaiObj.items(): # bu şekilde de key value bilgilerini yan yana yazdırabiliriz.
#    print(x,y)    

#sonuc = "marka" in hyundaiObj

#sonuc = len(hyundaiObj)

#hyundaiObj["renk"] = "silver grey"
#hyundaiObj.pop("renk") # .pop ile eklediğimiz bilgiyi silebiliyoruz.

#.popitem() bilgisi ise son ekleneni siler.

#del hyundaiObj["marka"] # belirtileni siler.

#print(sonuc)    

obj = hyundaiObj.copy() # referans .copy kopyasını alır.

obj["marka"] = "Opel"


hyundaiObj.update({   #.update yüklemek,değiştirmek istediğimiz şey.
    "marka": "Bmw",
    "renk": "Kırmızı"
})


print(obj)
print(hyundaiObj)



