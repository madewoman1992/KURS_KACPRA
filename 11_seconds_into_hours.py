# pewien program liczy czas tylko w sekundach i resetuje sie kazdego dnia, sprobuj zapisac w klasycznej formie czas przedstawiany w formacie 23400, 34200, 81000 wynikiem powinno byc 6:30, 9:30, 22:30
#  przygotuj program, ktory zmienu dowolna przekazana przez ustkowania wartosc do czytelenj postaci

seconds = int(input('How many seconds?'))

# minut = 60
# hour = 3600
#time_in_hours_1 = seconds // 3600
time_in_hours_2 = int((seconds / 60) // 60)
time_in_minutes = (seconds // 60) % 60


print(f'Now, is {time_in_hours_2}:{time_in_minutes}')


