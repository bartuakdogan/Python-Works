# Kendisine gönderilen 2 sayıdan hangisi büyük bulan fonksiyonu yazınız.
from turtle import up


def karsilastirma(a,b):
    if (a>b):
        print("a,b'den büyüktür.")
    elif (a<b):
        print("a,b'den küçüktür.")
    else:
        print("iki sayı birbirine eşittir.")  

karsilastirma(10,20)          
karsilastirma(10,10)          

# Kendisine gönderilen bir string bilgi içinde her karakter kaçar kez tekrarlanmış bulunuz.
# def karakterSayisiniBul(string):
#     return {letter: string.count(letter) for letter in string }

# sonuc = karakterSayisiniBul("flutter")
# print(sonuc)    


# Kendisine gönderilen list, command, position ve value bilgilerine göre liste üzerinde güncelleme yapınız.
  # [1,2,3], ("add, remove"), ("beginning | end"), value 
  # list_operation([1,2,3],"add","end","4") => [1,2,3,4]
  # list_operation([1,2,3],"remove","beginning") => [2,3]

# def update_list(liste,command,position,value=None):
#     if (command=="remove" and position=="end"):
#         return liste.pop()
#     elif (command=="remove" and position=="beginning"):
#         return liste.pop(0)
#     elif (command=="add" and position=="end"):
#         liste.append(value)
#         return liste
#     elif (command=="add" and position=="beginning"):
#         liste.insert(0,value)
#         return liste      

# sonuc = update_list([1,2,3],"add","end","4")
# sonuc = update_list([1,2,3],"remove","beginning")
# sonuc = update_list([1,2,3],"add","beginning","7")
# print(sonuc)

# Kendisine gönderilen renk isimlerinden içinde "blue" rengi varsa True döndüren fonksiyonu yazınız.

# def contains_blue(*args):
#     if "blue" in args:
#         return True
#     else:
#         return False 

# sonuc = contains_blue("blue","yellow","green")    
# print(sonuc)       