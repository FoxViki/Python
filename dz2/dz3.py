# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k
# ), не превосходящие числа N.
# 10 -> 1 2 4 8

N = int(input("Введите число N "))
k = 0
p = 2
while p**k <= N:
    rez = p**k
    print (rez)
    k += 1
    