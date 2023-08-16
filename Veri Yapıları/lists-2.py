diller = ['Python','C#','Java','Javascript']

sonuc = diller
sonuc = type(diller)

#diller[0] = 'Html'
diller[-1] = 'Html'
sonuc = diller
sonuc = len(diller)
sonuc = diller + ['Angular','Vuejs']

#if bloğu--> koşul ifadeleri
if "Python" in diller:
    print('bu değer listenin bir elemanı')

# döngüler
for x in diller:
    print(x)

del diller[0]
sonuc = diller

print(sonuc)
