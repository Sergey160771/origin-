# Дадана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100)* многочлена и записать в файл многочлен степени k.
# *Пример:*
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k=5 => 2*x^5 + 4*x^4 + 2*x^3 + 2*x^2 + 4*x + 5 = 0

import random

degree = int(input('введите степень многочлена  k: '))
coefficients = [random.randint(-100, 100) for i in range(0, degree + 1)]

polynomial = ''
for i in range(0, degree + 1):
    if degree - i > 1 and coefficients[1] != 0:
        polynomial += f'{coefficients[i]} + x^{degree - i} + '
    elif degree - i == 1 and coefficients[i] != 0:
        polynomial += f'{coefficients[i]}+x +'
    elif coefficients[i] == 0:
        polynomial += ''
    else:
        polynomial += f'{coefficients[i]} = 0'
polynomial = polynomial.replace('+ -', '- ')
print(polynomial)
with open('file4.txt', 'w') as data:
    data.write(polynomial)
