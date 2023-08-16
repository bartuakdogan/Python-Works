# 1- 3 ürün bilgisini (id,ad,fiyat) kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.
# 2- Ürün id bilgisini kullanıcıdan alıp ilgili ürün bilgisini gösterin.

urunler = {
          '100': {'ad': 'Iphone 11', 'fiyat': '15.999'}, 
          '101': {'ad': 'Iphone 13', 'fiyat': '25.999'}, 
          '102': {'ad': 'Iphone 14 Pro Max', 'fiyat': '59.999'}
          }



#id = input('id: ')
#ad = input('ad: ')
#fiyat = input('fiyat: ')

#urunler[id] = {
 #   'ad':ad,
  #  'fiyat':fiyat
#}

#id = input('id: ')
#ad = input('ad: ')
#fiyat = input('fiyat: ')

#urunler[id] = {
#    'ad':ad,
#    'fiyat':fiyat
#}

#urunler[id] = {
#    'ad':ad,
#    'fiyat':fiyat
#}

#id = input('id: ')
#ad = input('ad: ')
#fiyat = input('fiyat: ')

#urunler[id] = {
#    'ad':ad,
#    'fiyat':fiyat
#}

id = input('Aramak istediğiniz ürün id: ')
urun = urunler[id]

print(f'id: {id} ürün adı: {urun["ad"]} ürün fiyatı: {urun["fiyat"]}')




#print(urunler)





