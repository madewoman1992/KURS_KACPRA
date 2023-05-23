# Odbierz od użytkownika 3 liczby, wyświetl która z nich jest największa, a która z nich jest najmniejsza.

number_1 = int(input('Give me first number'))
number_2 = int(input('Give me a second number'))
number_3 = int(input('Give ma a third number'))

if number_1 > number_2 and number_1 > number_3:
    print(f' numer 1 i.e. {number_1} is the biggest')
elif number_2 > number_1 and number_2 > number_3:
    print(f' number 2 i.e. {number_2} is the biggest one')
else:
    print(f'number 3 i.e. {number_3} is the biggest one')

if number_1 < number_2 and number_1 < number_3:
    print(f' numer 1 i.e. {number_1} is the smallest')
elif number_2 < number_1 and number_2 < number_3:
    print(f' number 2 i.e. {number_2} is the smallest one')
else:
    print(f'number 3 i.e. {number_3} is the smallest one')