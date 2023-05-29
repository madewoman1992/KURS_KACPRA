# Napisz program, który pobierze od użytkownika ciąg znaków i zwróci ten sam tekst bez spacji oraz znaków interpunkcyjnych.
# STRINGI
import string

print(string.punctuation)


text = input('Give me some text, bro ')
lista = ('!', '.', ',', '?', ' ')

text1 = 0
for i in text:
    if i in lista:
        text = text.replace(i, '')
        print(text)




