'''
    player 1: 
        id           => 1
        name         => Cristiano Ronaldo
        yearOfBirth  => 1985
        nationality  => Portugal
        current_team => Portugal
        history      => Juventus,Real Madrid,Portugal

    player 2: 
        id           => 2
        name         => Lionel Messi
        yearOfBirth  => 1987
        nationality  => Argentina
        current_team => Barcelona,
        history      => Barcelona,Argentina,Portugal
'''

# 1- Yukarıda verilen bilgileri liste içerisinde saklayınız.

players = {'1': {'name': 'Cristiano Ronaldo', 'yearOfBirth': '1985', 'nationality': 'Portugal', 'current_team': 'Manchester United', 'history': ['Sporting CP', 'Real Madrid', 'Juventus', 'Manchester United']}, 
'2': {'name': 'Lionel Messi', 'yearOfBirth': '1987', 'nationality': 'Argentina', 'current_team': 'PSG', 'history': ['Barcelona', 'PSG']}}

id = input('Oyuncu ID: ')
name = input('Oyuncu Adı: ')
yearOfBirth = input('Doğum Yılı: ')
nationality = input('Uyruğu: ')
current_team = input('Takımı: ')
history = input('Oynadığı Takımlar: ')

players.update({
    id: {
        "name": name,
        "yearOfBirth": yearOfBirth,
        "nationality": nationality,
        "current_team": current_team,
        "history": history.split(',')

    


    }
})

id = input('Oyuncu ID: ')
name = input('Oyuncu Adı: ')
yearOfBirth = input('Doğum Yılı: ')
nationality = input('Uyruğu: ')
current_team = input('Takımı: ')
history = input('Oynadığı Takımlar: ')

players.update({
    id: {
        "name": name,
        "yearOfBirth": yearOfBirth,
        "nationality": nationality,
        "current_team": current_team,
        "history": history.split(',')

    


    }
})

print(players)








# 2- id' e göre arama yapınız.

#id = input('oyuncu id: ')

#sonuc = players.get(id)

#print(sonuc)



# 3- id' e göre bilgi kayıt siliniz.

id = input('silmek istediğiniz oyuncu id: ')

players.pop(id)

print(players)