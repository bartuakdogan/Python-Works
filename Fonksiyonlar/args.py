#liste = [10,20,30,40]

#def toplam(sayilar):
#    sonuc = 0
#    for i in sayilar:
#        sonuc += i
#    return sonuc    

#print(toplam(liste))

def toplam(*args):
    print(type(args))    # class=tuple   tuple yapıda.
    sonuc = 0
    for i in args:
        sonuc += i
    return sonuc 

print(toplam(10,20,30,40,50,60))         # bu şekilde birden fazla değişken atayabiliriz. ==>*args

