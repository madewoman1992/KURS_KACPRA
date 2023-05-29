# Zapytaj użytkownika o liczbę, w wyniku wyświetl informację czy jest ona liczba pierwsza

from math import sqrt, ceil


number = int(input('Give me a number'))

# ceil - sufit
# floor - podloga

is_prime = True
for div in range(2, ceil(sqrt(number)) + 1):
    if number % div == 0:
        is_prime = False
        break


if is_prime:
    print('Liczba jest pierwsza')
else:
    print('Libcza nie jest pierwsza')