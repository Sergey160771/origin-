# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

coordinate_X = float(input('Ведите координату X '))
coordinate_Y = float(input('Ведите координату Y '))
if coordinate_X > 0 and coordinate_Y > 0 :
    print('Точка находится в 1-й четверти')
elif coordinate_X < 0 and coordinate_Y > 0:
    print('Точка находится в 2-й четверти')
elif coordinate_X < 0 and coordinate_Y < 0:
    print('Точка находится в 3-й четверти')
elif coordinate_X > 0 and coordinate_Y < 0:
    print('Точка находится в 4-й четверти')
else:
    print('Не правельная точка! Не соответствует условию задачи!')    

