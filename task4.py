# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
a = int(input('Введите число: '))
b = '' # остатки от деления на 2
while a>0:
    b = str(a%2)+b
    a = a//2
print(b)

# Второй вариант
# a = int(input('Введите число: '))
# print(bin(a))