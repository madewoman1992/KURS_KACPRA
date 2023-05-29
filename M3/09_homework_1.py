# Napisz program, który stworzy listę zawierającą imiona 5 twoich znajomych.
# Następnie wyświetl imiona twoich znajomych w kolejności alfabetycznej.


imiona = []

for i in range(5):
    pytanie= input('Podaj imiona swoich znajomych: ')
    imiona.append(pytanie.split(' '))
    imiona.sort()

print(imiona)
