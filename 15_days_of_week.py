
#  Napisz program, który odbierze od użytkownika numer dnia tygodnia,
# a następnie wyświetli jego nazwę np. dla wartości
# 1 wyświetli “poniedziałek”, a dla wartości 7 wyświetli “niedziela”

number_of_day_of_week = int(input('What is the number of day of week?'))

if number_of_day_of_week == 1:
    print('Its Monday')
elif number_of_day_of_week == 2:
    print('Its Tuesday')
elif number_of_day_of_week == 3:
    print('Its Wednesday')
elif number_of_day_of_week == 4:
    print('Its Thursday')
elif number_of_day_of_week == 5:
    print('Its Friday')
elif number_of_day_of_week == 6:
    print('Its Saturday')
elif number_of_day_of_week == 7:
    print('Number is not wrong!')



match number_of_day_of_week:
    case 1: print('poniedzialek')
    case 2: print('wtorek')
    case _: print('wartosc nieprawidlowa')
