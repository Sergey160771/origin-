# Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве.

coordinate_XA = float(input('Ведите координату X точки A: '))
coordinate_YA = float(input('Ведите координату Y точки A: '))
coordinate_XB = float(input('Ведите координату X точки B: '))
coordinate_YB = float(input('Ведите координату Y точки B: '))
distance = abs((coordinate_XA - coordinate_XB)**2 + (coordinate_YA - coordinate_YB)**2)
print(f'Растояние от точки A до точки B = {distance}')

