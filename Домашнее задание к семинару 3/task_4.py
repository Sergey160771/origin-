# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#     Пример:
#     - 45 -> 101101
#     - 3 -> 11
#     - 2 -> 10

number_binary = ""
number = int(input('Введите число в десятичной системе счисления: '))
while number != 0:
    number_binary = str(number % 2) + number_binary
    number //= 2
print(f'Число в двоичной системе счисления равно {number_binary} ')
