#Odbierz od użytkownika liczbę,
# a następnie wyświetl informację czy jest to liczba palindromiczna.
# Aby sprawdzić jej długość sprawdź podpowiedź: len(liczba)

number = str(input(f'Give me a number'))

# print(len(number))

if number == number[::-1]:
    print(f' Your number is palindromic')
else:
    print('Number is not palindromic')
