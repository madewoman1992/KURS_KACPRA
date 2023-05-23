# odbierz od U dwa dowolne punkty na płaszczyźnie x1,y1, x2,y2, które tworzą odcinek. Znajdz jego srodek
# wypisz pole oraz promień okręgu, którego ten odcinek jest średnicą

x1 = float(input('Give me value od x1'))
x2 = float(input('Give me value od x2'))
y1 = float(input('Give me value od y1'))
y2 = float(input('Give me value od y2'))

the_middle_of_X = float((x1 + x2) / 2)
the_middle_of_Y = float((y1 + y2) / 2)

print(f'The middle of segment is {the_middle_of_X},{the_middle_of_Y}')

r = (((x1 - x2)**2 + (y1 - y2)**2)**1/2) / 2
print(f' The r of this circle is {r}')

area = 3.14 * r**2
print(f'Area of circle is {area}')

# zastanow sie jakie pole i obwod ma prostokat, ktorego ten odcinek jest przekatna

diagonal = ((x1 - x2)**2 + (y1 - y2)**2)**1/2)
area_of_rectangle = 1/2 * diagonal**2 *
# nieskonczone


