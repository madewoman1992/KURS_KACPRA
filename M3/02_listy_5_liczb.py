# Napisz program, w którym zapytasz użytkownika o 5 liczb.
# 1. Każdą z liczb dodajemy do listy.
# 2. Zwracamy najmniejszy, największy element oraz średnią arytmetyczną wszystkich wprowadzonych liczb.

numbers = []

for _ in range(5):
    number = input('Give me a number: ')
    numbers += number

numbers = [int(x) for x in numbers]

print(numbers)

print(min(numbers))
print(max(numbers))
print(sum(numbers) / len(numbers))


