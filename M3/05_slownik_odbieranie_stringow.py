#  Przygotuj program, który odbierze od użytkownika dowolny string,
#  a następnie zwróci słownik zawierający informację ile razy wystąpiło każde słowo.
#  Np: “raz raz dwa trzy”. powinno zwrócić słownik { “raz”: 2, “dwa”: 1, “trzy”: 1 }

words = input('Podaj slowa: ')
word = words.split(' ')
slownik = dict()
liczby = []

for i in word:
    liczby1 = str(word.count(i))
    liczby += liczby1


slownik = dict(zip(word, liczby))
print(slownik)







