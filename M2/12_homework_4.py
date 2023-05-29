# Napisz kod, który przejdzie po wszystkich znakach łańcucha znaków i wyświetli osobno
# każdy znak oraz odpowiednik z tablicy ASCII za pomocą funkcji ord()

sentence = input('Podaj zdanie')

for i in sentence:
    print(i, ord(i), end='\n')

