# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.(одинаковый размер уравнений)*
lst1 = []
path1 = 'file1.txt'
date1 = open(path1, 'r')
for line in date1:
    print(line)
    nums1 = line.split()
for i in nums1:
    if i.isdigit() or i == '-':
        lst1.append(i)
    if i == ' ':
        break

i = 0
while lst1.count('-') != 0:
    if lst1[i] == '-':
        lst1[i] += lst1[i + 1]
        lst1.pop(i + 1)
        i = 0
    i += 1
print(lst1)
date1.close()

lst2 = []
path2 = 'file2.txt'
date2 = open(path2, 'r')
for line in date2:
    print(line)
    nums2 = line.split()
for j in nums2:
    if j.isdigit() or j == '-':
        lst2.append(j)
    if j == ' ':
        break

j = 0
while lst2.count('-') != 0:
    if lst2[j] == '-':
        lst2[j] += lst2[j + 1]
        lst2.pop(j + 1)
        j = 0
    j += 1
print(lst2)
date2.close()

result = [int(lst1[i]) + int(lst2[i]) for i in range(len(lst1))]
result1 = f'{result[0]} * x^ 3 + {result[1]} * x^ 2 + {result[2]} * x + {result[3]}'

print(result)
result1 = result1.replace('+ -', '- ')
print(result1)

with open('file3.txt', 'w') as data:
      data.write(result1)

