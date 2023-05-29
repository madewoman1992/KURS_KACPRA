# Poniżej wypisz małymi literami tylko te słowa z podanego zdania, które zaczynają się i kończą na tą samą literę.

sentence = input('Give me a sentence')

new_sentence = ''

for word in sentence.split(' '):
    if word[0].lower() == word[-1].lower():
        print(word)


