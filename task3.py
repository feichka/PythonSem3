# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

lst = [1.1, 1.2, 3.1, 5, 10.01]
max = 0
min = 100
for i in range(len(lst)):
    a = (lst[i]*100)%100
    if a > max:
        max = a
    if a<min and a != 0:
        min = a
    print(round(a,2), end = ' ')
# print()
# print(max)
# print()
# print(min)
res = (max-min)/100
print(res)
