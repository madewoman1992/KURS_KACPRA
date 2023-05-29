#  Przygotuj program, który odbierze od użytkownika dowolny string,
#  a następnie zwróci słownik zawierający informację ile razy wystąpiło każde słowo.
#  Np: “raz raz dwa trzy”. powinno zwrócić słownik { “raz”: 2, “dwa”: 1, “trzy”: 1 }

sentence = input('Podaj slowa: ')
words = sentence.split(' ')
word_counter = {}

for word in words:
    word_counter.update({word: word_counter.get(word, 0) + 1})

print(word_counter)
