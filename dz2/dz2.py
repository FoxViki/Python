# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

s = 12
p = 27

for x in range(s//2+1):
    y = s - x
    if p == x*y:
        print(x, y)
    





# y = abs(int(input('Введите второе натуральное число Y от 1 до 1000 ')))
# if x < 1 or x > 1000 or y < 1 or y > 1000:
#     print('Вы ввели число не из заданного диапазона!')
# else:
#     S = x + y
#     P = x * y
#     stop = 0
#     for i in range(1001):
#         if stop != 1:
#             for j in range(1001):
#                 if stop != 1:
#                     if i * j == P and i + j == S:
#                         print(i, j)
#                         stop = 1
#             else:
#                 j = 1001
#         else:
#             i = 1001






# На входе:
# s = 12
# p = 27

# На выходе:
# 3 9
# 9 3

# s = 12
# p = 27

# # for i in range(s+1):
# #     if i*(s-i) == p:
# #         print(i, s-i)
# #         break

# for i in range(s//2+1):
#     if i*(s-i) == p:
#         print(i, s-i)




# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

# N = abs(int(input('Введите число N ')))
# stop = 0
# P = 2
# for i in range(N):
#     if stop != 1:
#         P = P ** i
#         if P <= N:
#             print(P, end=' ')
#             P = 2
#         else:
#             stop = 1
#     else:
#         i = N