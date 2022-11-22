# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarter_number = int(input('Введите номер четверти '))
if quarter_number == 1:
    print('X > 0 and Y > 0')
elif quarter_number == 2: 
    print('X < 0 and Y > 0') 
elif quarter_number == 3:  
    print('X < 0 and Y < 0') 
elif quarter_number == 4:  
    print('X > 0 and Y < 0') 
else:
    print('Такой четверти не существует')           