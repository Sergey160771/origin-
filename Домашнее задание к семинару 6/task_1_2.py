# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension.

n = input('Введите вещественное число: ')
sum = sum(map(int, n.replace('.', '')))
print (sum)