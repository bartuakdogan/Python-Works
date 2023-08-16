import enum


markalar = ["bmw","opel","mercedes"]

#index = 0

#for marka in markalar:
#   print(f"{index+1}-{markalar[index]}")
#    index +=1

#enumarate

#obj1 = enumerate(markalar)

#print(type(obj1))
#print(list(obj1))

#for index,value in enumerate(markalar,1):
#    print(f"{index}-{value}")

#zip

liste1 = (1,2,3,4,5)
liste2 = ('iphone','samsung','xiaomi','oppo','LG')
print(list(zip(liste1,liste2)))

for item in zip(liste1,liste2):
    print(item)
