# zapytaj uzytkownika o liczbe i wyswoetl info czy jest to liczba dodatnia, ujemna czy zero

number = float(input('Which numer do you have?'))

if number > 0:
    print(f'Your number {number} is positive')
elif number == 0:
    print(f'Your number {number} is 0')
else:
    print(f'your number {number} is negative')

