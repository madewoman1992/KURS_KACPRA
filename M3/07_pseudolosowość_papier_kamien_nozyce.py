# Korzystając z dokumentacji oraz Google:
# 1. Stwórz tuplę zawierającą papier, kamień, nożyce
# 2. Zapytaj użytkownika o jego wybór (p, k, n)
# 3. “Wylosuj” jeden z elementów z tupli i wyświetl informację kto
# wygrał. Użytkownik czy komputer.

import random


from random import randint, choices, choice

game = ('papier', 'kamien', 'nozyce')
wybor = input('Co wybierasz: papier, kamien czy nozyce ')
komputer = ()


for i in range(1):
    komputer = random.choice(game)
    print(f' Komputer wybral {komputer}')
    if komputer == wybor:
        print('Remis')
    elif komputer == 'papier' and wybor == 'kamien':
        print('Komputer wygral!')
    elif komputer == 'papier' and wybor == 'nozyce':
        print('Ty wygrales')
    elif komputer == 'kamien' and wybor == 'papier':
        print('Ty wygrales!')
    elif komputer == 'kamien' and wybor == 'nozyce':
        print('Komputer wygral')
    elif komputer == 'nozyce' and wybor == 'papier':
        print('Ty wygrales!')
    elif komputer == 'nozyce' and wybor == 'kamien':
        print('Ty wygrales')

