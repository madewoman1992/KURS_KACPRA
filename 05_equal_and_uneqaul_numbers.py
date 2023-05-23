number_1 = float(input('Give me one number'))
number_2 = float(input('Give me second number'))

if number_1 == number_2:
    print('Number are equal')
elif number_1 > number_2:
    print(f'{number_1} is bigger than {number_2}')
elif number_2 > number_1:
    print(f'{number_2} is bigger than {number_1}')

# na koncu ze sa rowne jako else