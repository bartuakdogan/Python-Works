# Identitiy Operator: is (adresler önemli)

#x = y = [1, 2, 3]
#z = [1, 2, 3]

#print(x == y) #True
#print(x == z) #True
#print(x is y) #True çünkü adresler aynı x = y
#print(x is z) #False,içindekiler aynı ancak adresler farklı x eşit değil z

x = [1, 2, 3]
y = [2, 4]

del x[2]
y[1] = 1
y.reverse()

print(x == y) #True ikisi de aynı elemanlara sahip oldu.
print(x is y) #False adresler farklı.(x!=y)
print(x is not y) #True x, y değil mi.Evet değil.


# Membership Operator: in

x = ['apple','banana']
print('banana' in x) #True(banana elemanı x'in içinde mi?)
