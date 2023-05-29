# to samo zadania co 9, ale rozwiazane przez Kacpra



sentence = input('Give me a text')
new_sentence = ''

for char in sentence:
    if char.isnumeric() or char.isalpha():
        new_sentence = new_sentence + char

print(new_sentence)