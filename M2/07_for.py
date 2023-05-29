# 1. Z podanej tupli liczb wyświetl te, które są podzielne przez 4 i te które są podzielne przez 5.

numbers = (1, 2, 3, 5, 20, 58, 30, 12, 16)

for number in numbers:
        if number % 4 == 0 or number % 5 == 0:
            print(number)

# 2. Z podanej tupli imion o różnej długości wyświetl tylko te które są dłuższe niż 5 znaków.
# Długość imienia sprawdź funkcją len()

names = ('Karolina', 'Justyna', 'Paulina', 'Agnieszka', 'Monika', 'Ala', 'Ola', 'Jan')

for name in names:
    if len(name) > 5:
        print(name)

# 3. Umieszczając pętle for w drugiej pętli for wyświetl trójkąt jak w przykładzie:
# 1 2 3 4
# 1 2 3
# 1 2
# 1


for counter in reversed(range(1,5)):
#    print(counter) # to przyjmuje warosci 4321
    for digit in range(1, counter+1):
        print(digit, end=' ')
    print()
