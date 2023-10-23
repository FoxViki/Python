# Даны два неупорядоченных набора целых чисел
# (может быть, с повторениями). Выдать без повторений
# в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# На вход подается 2 числа через пробел: n m
# n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем подаются элементы каждого множества
# через пробел в виде строки. ! Писать input() не надо

# Пример

# На входе:
# var1 = '5 4' # количество элементов первого и второго множества
# var2 = '1 3 5 7 9' # элементы первого множества через пробел
# var3 = '2 3 4 5' # элементы второго множества через пробел
# На выходе:
# 3 5


var1 = '5 4'
var2 = '10 20 30 40 50'
var3 = '10 20 30 40 50'
#var2 = var2.replace(' ', '')
#var3 = var3.replace(' ', '')
print(var2)
print(var3)
set1 = set(var2)
set2 = set(var3)
print(set1)
print(set2)
set1.remove(' ')
set2.remove(' ')
print(set1)
print(set2)
set_ob = sorted(set1.intersection(set2))
my_list = list(set_ob)
result = " ".join(my_list)
print(result)

#set1 = set(map(int, var2.split()))
#set2 = set(map(int, var3.split()))
# set3 = set1.intersection(set2)
#print(len(set1))
#print(len(set2))
# print(a)
# print(b) 

