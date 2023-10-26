# найти факториал числа n через рекурсию

# n = 5
# def factorial(n):
#     if n == 1:
#         return n
#     return n * factorial(n-1)
# print(factorial(n))

# мой вариант
# def Factorial(n):
#     if (n == 0):
#         return 1
#     else:
#         return n * Factorial(n - 1)
# print (Factorial(n))

# Задача No31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ...,
# где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7 Output: 21

# index = 7

# def fibonacci(index):
#     if index == 0:
#         return 0
#     if index == 1:
#         return 1
#     return fibonacci(index-1) + fibonacci(index-2)
# print(fibonacci(7))



# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).


# quantity = 4
# def function(quantity):
#     if quantity == 0:
#         return '+'         #пустая строка
#     number = input("Введите число ")
#     return function(quantity-1) + number # если прямой порядок то слагаемые меняют местами
# print(function(4))

# Задача №35. Общее обсуждение
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# def prov(a, b):
#     if (int(a/b == a) & int(a/b == 1)):
#         return "a - простое число"
#     else:
#         return "a - составное число"
    
# def prime(number):
#     n = number
#     counter = 0
#     for i in range(1, n + 1):
#         if n % i == 0:
#             counter += 1
#     return 'Простое число' if counter == 2 else 'Составное число'

# n = 5
# print(prime(6))

# 33/Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

my_list = [5, 2, 3, 4, 5, 3, 4]

for i in range(len(my_list)):
    if my_list[i] >= 4:
        my_list[i] = 2
print(my_list)


