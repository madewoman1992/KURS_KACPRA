#  Napisz program, który zliczy słowa oraz znaki w podanym przez użytkownika zdaniu

sentence = input('Give me a sentence ')

numbers_of_words = len(sentence.split(' '))

print(numbers_of_words)

number_of_letters = len(sentence)
print(number_of_letters)