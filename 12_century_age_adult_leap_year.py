# Przygotuj program, który na podstawie wieku urodzenia danej osoby, odpowie ile ta osoba ma lat,
# czy jest pełnoletnia oraz czy rok w którym się urodziła był rokiem przestępnym.
# Zwróć uwagę, że taki rok nie zawsze przypada co cztery lata :)
# Rok bieżący możesz przechowywać w jednej zmiennej zadeklarowanej na początku programu.



current_year = 2023
year_of_birth = int(input('In which year were yor born?'))

age = current_year - year_of_birth

if age >= 18:
    print(f'You are {age} years old and you are adult')
else:
    print(f'You are {age} years old and you are not adult')

if year_of_birth % 4 == 0 and year_of_birth % 100 != 0 or year_of_birth % 400 == 0:
    print(f'The year in which you were born is leap year')
else:
    print(f'The year in which you were born is not a leap year')





