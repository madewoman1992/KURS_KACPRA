# 1. Napisz program, który odbierze od użytkownika liczbę całkowitą,
# a następnie wyświetli na ekranie wszystkie liczby parzyste
# od 2 do tej liczby. Wyświetl wszystkie te liczby oddzielone przecinkami.

number = int(input('Give me number'))

for n in range(2, number + 1):
    if n % 2 == 0:
        print(n, end=',')
