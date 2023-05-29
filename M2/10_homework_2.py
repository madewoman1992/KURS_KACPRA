# 2. Poniżej wyświetl sumę, liczbę, średnią oraz iloczyn tych liczb tj. z zadania 1
import math

number = int(input('Give me number'))

for n in range(2, number + 1, 2):
    total = sum(range(2, number + 1, 2))
    amount = len(range(2, number + 1, 2))
    average = float((sum(range(2, number + 1, 2))) / len(range(2, number + 1, 2)))
    product = n * n



print(f'Suma tych liczb wynosi {total}')
print(f'Liczba tych liczb to {amount}')
print(f'średnia to to {average}')
print(f'product to to {product}')
