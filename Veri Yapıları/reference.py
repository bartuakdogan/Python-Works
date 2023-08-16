# value types ==> string,number(float,integer) için

x = 5
y = 25

x = y

y = 10

#print(x,y)    # y'nin üzerinde yaptığımız değişiklik x'i etkilemedi.

# reference types ==> list
a = ["apple","banana"]
b = ["apple","banana"]

a = b

b[0] = "grape"

print(a,b)      # reference types'ta value'dakinin aksine b'de yaptığımız değişiklik a'yı da etkiledi.aynı referansa taşıyor çünkü.

 