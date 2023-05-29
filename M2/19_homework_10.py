# Odbierz od użytkownika zdanie, a następnie wypisz je w taki sposób by poszczególne wyrazy były zapisane raz MAŁYMI raz WIELKIMI
# literami.

sentence = input('Give me a sentence')

new_sentence = ''

for counter, word in enumerate(sentence.split(' ')):
    new_word = word.upper()
    if counter % 2 == 0:
        new_word = word.lower()

    new_sentence = f'{new_sentence} {new_word}'

print(new_sentence)