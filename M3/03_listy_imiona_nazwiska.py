# Napisz program, w którym odbierzesz od użytkownika imiona
# oraz nazwiska rozdzielone przecinkami, w odpowiedzi powinny wyświetlić
# się poprawnie zapisane imiona bez powtórzeń posortowaną w kolejności Z-A

imiona_nazwiska = []


for _ in range(2):
    imie = input('Podaj imie ')
    nazwisko = input('Podaj nazwisko ')
    imiona_nazwiska.append(imie.split(' '))
    imiona_nazwiska.sort(reverse=True)

print(imie, ',', nazwisko)

print(imiona_nazwiska)




#print(pytanie.sort(reverse=True))



#        range(2):
#    pytanie_o_dane_osobowe = input('Podaj mi imie oraz nazwisko: ')
#    dane_osobowe += pytanie_o_dane_osobowe.split(',')
#    same_imiona += pytanie_o_dane_osobowe.split(' ')


#print(same_imiona.sort(reverse=True))





# print(dane_osobowe.sort(reverse=True))

