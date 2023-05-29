# Przygotuj tuplę przechowującą imię, nazwisko oraz wiek osoby. Następnie wyświetl te dane w postaci:
# Imię: John
# Nazwisko: Smith
# wiek: 40

informations = ('Imie: John', 'Nazwisko: Smith', 'Wiek: 40')

for i in informations:
    print(i, end='\n')

# Zadeklaruj tuple w postaci a=((1,2,3), (4,5,6), (7,8,9)), a następnie przechodząc po nich za pomocą pętli for wyświetl:
# 1+ 2 + 3 = 6
# 4 + 5 + 6 = 15
# 7 + 8 + 9 = 24
print('-----' * 30)

a = ((1,2,3) , (4,5,6), (7,8,9))

for i in a:
    print(i[0], '+', i[1], '+', i[2], '=', sum(i))
