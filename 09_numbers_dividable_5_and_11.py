# napisz program, który wyświetli informację czy liczba jest podzielna przez 5,11 lub przez 5 i 11


number = int(input('Give me a number'))

# if number % 5 == 0:
#    print(f'Number {number} is dividable by 5')
#elif number % 11 == 0:
#   print(f'Number {number} is dividable by 11')
#elif number % 5 == 0 and number % 11 == 0:
#   print((f'Number {number} is dividable by 5 and 11'))
#else:
#   print(f'Number {number} is not dividable by 5 or 11')

#UWAGA TU TRZEBA NAJPIERW SPRAWDZIC CZY JEST PODZIELNA PRZEZ 5 I 11 BO INACZEJ NIE WYKONA TAMTYCH


if number % 5 == 0 and number % 11 == 0:
    print(f'Number {number} is dividable by 5 and 11')
elif number % 5 == 0:
    print(f'Number {number} is dividable by 5')
elif number % 11 == 0:
    print(f'Number {number} is dividable by 11')
else:
    print(f'Number {number} is not dividable by 5 or 11')
