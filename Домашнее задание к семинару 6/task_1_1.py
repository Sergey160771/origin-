 # Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# *Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

number = int(input('Введите число N: '))
number_list = {}
number_list = {i: 3 * i + 1 for i in range(1, number + 1)}
print(number_list)