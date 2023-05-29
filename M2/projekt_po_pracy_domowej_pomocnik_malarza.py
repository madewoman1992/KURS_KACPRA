from math import ceil


walls = int(input('How many walls do you have to paint? '))


print('If you want to assume previous value, press enter')
area_of_walls = 0
width = 0
height = 0

for i in range(walls):
    width = int(input('Give me a width of next wall '))
    height = input('Give ma a height of next wall ') or height
    # height = int(height)
    # print(height)
    area_of_walls += width * int(height)
print(area_of_walls)

layer_of_size = 2
print(f' Ilosc wart gruntu: {layer_of_size}')
layer_of_paint = 3
print(f' Ilosc wart farby: {layer_of_paint}')

productivity_of_size = ceil(area_of_walls * 2 / 5)
productivity_of_layer = ceil(area_of_walls * 3 / 13)

print(f' Potrzebujesz {productivity_of_size} litrow gruntu i {productivity_of_layer} litrow farby')







