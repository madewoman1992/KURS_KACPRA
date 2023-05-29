
translation = input('Write down, which language do you want to translate into, Polish or English ? ')
word = input('Give a word which one do you want to translate: ')

dictionary = {'pies':'dog', 'owoc':'fruit', 'auto':'car', 'biurko':'desk', 'kuchnia':'kitchen'}


for PL, EN in dictionary.items():
    if word == PL:
        print(EN)
    elif word == EN:
        print(PL)
    elif word == PL and word == EN:
        print('Word is not in dict')


