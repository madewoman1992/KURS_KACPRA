# Poniżej wyświetl wszystkie słowa ze zdania z usuniętymi samogłoskami.


sentence = input('Give me a sentence')
vowels = ('aeiuoy')
new_sentence = ''

for word in sentence:
    if word.lower() not in vowels:
        new_sentence += word

print(new_sentence)

