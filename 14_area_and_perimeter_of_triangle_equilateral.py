
# Zapytaj użytkownika o długość boku trójkąta równobocznego.
# Jakie jest pole i obwód tego trójkąta?

lenght_of_one_side_of_trangle = int(input('What is the lenght of one side of triangle?'))

from math import sqrt

area_of_equilateral_triangle = (lenght_of_one_side_of_trangle** 2 * sqrt(3)) / 4

perimeter_of_equilateral_triangle = 3 * lenght_of_one_side_of_trangle

print(f' Area of equilateral trangle is {area_of_equilateral_triangle} and perimeter is {perimeter_of_equilateral_triangle}')



