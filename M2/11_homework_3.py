#Odbierz od użytkownika liczbę, a następnie wyświetl tę liczbę podniesioną do potęgi od 2, 3, 4 oraz 5.
# Użyj pętli for!

number = int(input('Podaj mi liczbę!'))
result = number

for power in range(4):
    result = result * number
    print(f'Liczba {number} podniesiona do potego {power + 2} wynosi {result}')


print(tuple(range(4)))