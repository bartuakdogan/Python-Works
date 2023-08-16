# list
# tuple
# dictionary
# sets ==> indexlenemez,sıralanamaz.(ekleme yaparken var olanı değiştirmek istemiyorsak,sıra önemli değilse set'i kullanabiliriz.)
#      ==> tuple dan farkı ekleme yapılabilir olmasıdır. 

meyveler = { 'elma','kiraz','kavun','üzüm' }
sebzeler = {'salatalık','domates'}


#for x in meyveler:
#    print(x) 

#sonuc = 'elma' in meyveler

meyveler.add('karpuz')

meyveler.update(['vişne','muz'])

meyveler.remove('karpuz')


sonuc = meyveler.union(sebzeler) # iki set i birleştiririz.(.union() komutu ile.)

#sonuc = len(meyveler)


print(sonuc) 
