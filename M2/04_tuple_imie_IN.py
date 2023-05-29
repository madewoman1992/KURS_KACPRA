imiona = ('Karolina', 'Agata', 'Monika', 'Ola')

twoje_imie= input('Jak masz na imię?')

#if twoje_imie == imiona[0] or twoje_imie == imiona[1] or twoje_imie == imiona[2] or twoje_imie == imiona[3]:
#   print(f'Twoje imie tj. {twoje_imie} znajduje sie na liście')
#else:
#    print(f'Twoje imie tj. {twoje_imie} nie znajduje sie na liscie')

if twoje_imie in imiona:
    print(f' Twoje imie tj. {twoje_imie} jest nw tupli')
else:
    print(f' Twoje imie tj. {twoje_imie} nie jest w tupli')

#tu rozroznia wielkosc liter!!!!