# Napisz program, który „wylosuje” liczbę z przedziału od 1 do 100,
# a następnie korzystając z biblioteki math wypisze:
# kwadrat i pierwiastek kwadratowy zaokrąglony w dół i w górę tej liczby.

import math
from math import sqrt
import random

liczba = float(random.randrange(1, 3,))
print(liczba)
kwadrat_w_gore = math.ceil(liczba**2)
pierwiastek_w_gore = math.ceil(sqrt(liczba))
print(f' Kwadrat w gore od {liczba} to {kwadrat_w_gore}, a pierwiastek w gore to {pierwiastek_w_gore}')

kwadrat_w_dol = math.floor(liczba**2)
pierwiastek_w_dol = math.floor(sqrt(liczba))
print(f' Kwadrat w dol od {liczba} to {kwadrat_w_dol}, a pierwiastek w dol to {pierwiastek_w_dol}')


