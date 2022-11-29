# Задайте список из n чисел последовательности (1 + (1/n))^n и выведите на экран их сумму.
#  *Пример:*
#  - Для n = 3:  {1: 2, 2: 2.25 , 3: 2.37}

number = int(input('Введите число N: '))
number_list = {}
sum = 0
for i in range(1, number + 1):
    number_list[i] = round((1+(1/i)) ** i, 3)
    sum += number_list[i]
print(number_list)
print(f'Сумма значений словоря = {sum}')
