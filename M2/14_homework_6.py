# Stwórz tuple zawierającą liczby podzielne przez 6 z zakresu od 12 do 1024 i odpowiedz na poniższe pytania:
# ➔ Ile jest tych liczb?
# ➔ Wyświetl trzy pierwsze liczby
# ➔ Przedostatni element
# ➔ Co szósty element licząc od czwartego
# ➔ Co trzeci element licząc od końca
# ➔ Ile wynosi średnia 10 ostatnich wartości?


number = tuple(range(12, 1025, 6))
print(len(number))
print(number[0:3])
print(number[-2])
print(number[3::6])
print(number[::-3])

suma = sum(number[-10::])
average = int(suma / 10)
print(average)
