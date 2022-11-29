# Реализуйте алгоритм нахождения(генерации) рандомного(случайного) числа.(Не используя библиотеки связанные с рандомом)

import datetime

randomNumber = datetime.datetime.now().microsecond % 100
print(f'Случайное число = {randomNumber}')
