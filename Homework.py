# 1)Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# from random import randint
# n = [randint(1, 9) for i in range(5)]
# print(n)
# sum = 0
# for i in range(len(n)):
#     if i % 2 != 0:
#         sum += n[i] 
# print(f'Сумма элементов стоящих на нечетных позициях = {sum}')

# 2)Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# from random import randint
# number = int(input('Введите размер списка: '))
# list = []
# list2 = []
# for i in range(number):
#     list.append(randint(0, 9))
# for i in range(len(list)):
#     while i < len(list)/2 and number > len(list)/2:
#         number = number - 1
#         a = list[i] * list[number]
#         list2.append(a)
#         i += 1
# print(list)
# print(list2)

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# from random import uniform
# num = int(input('Введите размер списка: '))
# list = []
# for i in range(num):
#     fl = uniform(0, 99)
#     list.append(round(fl, 2))
# min = list[0]
# max = 0
# for i in range(len(list)):
#     if max < list[i]:
#         max = list[i]
#     if min > list[i]:
#         min = list[i]
# dif = (max - int(max)) - (min - int(min))
# print(list)
# print(max, min)
# print(round(dif,2))

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

s = ""
n = int(input("Введите число для преобразовывания: "))
while n != 0:
    s = str(n % 2) + s
    n //= 2
print(s)