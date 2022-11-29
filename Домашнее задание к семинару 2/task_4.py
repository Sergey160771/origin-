# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

num = int(input('Введите число: '))
numbers = []
for i in range(-abs(num), abs(num) + 1, 1):
    numbers.append(i)

result = 1
with  open('file.txt', 'r') as data:
    for position in data:
        result *= numbers[int(position)]
print(f'Произведение элементов из списка {numbers} на позициях указанных в файле file.txt  = {result}')
