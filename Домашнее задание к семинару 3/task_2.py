# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#    Пример:
#    - [2, 3, 4, 5, 6] => [12, 15, 16];
#    - [2, 3, 5, 6] => [12, 15]

list = [2, 3, 4, 5, 6, 8, 10 ,4]
list2 = []
number = len(list)
for i in range(number):
    while i < len(list) / 2 and number > len(list) / 2:
        number -= 1
        a = list[i] * list[number]
        list2.append(a)
        i += 1
print(list)
print(list2)
