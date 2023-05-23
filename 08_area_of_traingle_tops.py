# Przygotuj program, który obliczy pole trójkąta o podanych trzech wierzchołkach, o każdy wierzchołek pytaj osobno

top_A_1 = float(input('Give me value of top A1'))
top_A_2 = float(input('Give me value of top A2'))

top_B_1 = float(input('Give me value of top B1'))
top_B_2 = float(input('Give me value of top B2'))

top_C_1 = float(input('Give me value of top C1'))
top_C_2 = float(input('Give me value of top C2'))

area_of_triangle = (abs(1/2 * ((top_B_1 - top_A_1) * (top_C_2 - top_A_2) - (top_B_2 - top_A_2) * (top_C_1 - top_A_1))))

print(f'Area of triangle is {area_of_triangle}')
