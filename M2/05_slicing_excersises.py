
# Za pomocą range i tuple stwórz listę liczb od 1 do 100
numbers = tuple(range(1, 101))
print(numbers)

# Wyciągnij tylko pierwsze 10 liczb.
print(numbers[0:10])

# Wyciągnij tylko ostatnie 10 liczb. (minus od końca)
print(numbers[-10:])

# Wyciągnij z tej listy tylko wartości nieparzyste
print(numbers[::2])

# Wyciągnij z listy tylko wartości parzyste w kolejności od największej do najmniejszej.
print(numbers[::-2])


