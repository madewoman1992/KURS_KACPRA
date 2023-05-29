# 1. Poproś użytkownika o podanie imienia.
# W zależności od jego ostatniej litery wyświetl “Witam Panią” lub “Witam Pana”.

name = input('What is your name?')

if name.endswith('a'):
    print('Hello Miss')
else:
    print('Hello Sir')

# 2. Napisz program generujące bardzo “silne” hasła.
# Zamień każdą literę “a” na @ oraz każdą literę s na $.

password = input('Give me you password')

password = password.lower().replace('a', '@')
password = password.lower().replace('s', '$')

print(password)

#czy nie dalo by sie wprowadzic nowej kolekji? no new_pass

# 3. Policz ile razy w zdaniu “Pies to najlepszy przyjaciel człowieka, lecz nie każdy pies o tym wie”. Wystąpiło słowo “pies”

sentence = 'Pies to najlepszy przyjaciel człowieka, lecz nie każdy pies o tym wie'

count = sentence.lower().count('pies')
print(count)

# Poszukaj innych funkcji niż upper i lower i spróbuj ze zdania:
# “12 kilogramów jabłek, 10 kilogramów gruszek, 20 kilogramów śliwek”
# policzyć ile łącznie razem ważą zakupione produktu. (spacje przed kilogramami muszą być :)

quote = '12 kilogramów jabłek, 10 kilogramów gruszek, 20 kilogramów śliwek'

quote = quote.split(' ')
quote = quote[::3]
sum = int(quote[0]) + int(quote[1]) + int(quote[2])

print(sum)

