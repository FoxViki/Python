# 2.Заполните массив элементами арифметической прогрессии.
# Её первый элемент a1 , разность d и количество элементов n
# будет задано автоматически. Формула для получения n-го члена
# прогрессии: an = a1 + (n-1) * d.

# Пример

# На входе:

# a1 = 2
# d = 3
# n = 4

# ap=list(n)
# print(type(ap))
# list_arr[0]=a1
# list_arr.append(list_arr[0])
# for i in range(1, n+1):
#     list_arr[i]=a1 + (i-1)*d
#     list_arr.append(list_arr[i])
# print(list_arr)

# list_1 = list() # создание пустого списка
# for i in range(n): # цикл выполнится 4 раз
#     a=
# a = int(input()) # пользователь вводит целое число
# list_1.append(a)
a1 = 7
d = 2
n = 5
arr=[]
for i in range(n):
    c = a1 + i * d
    arr.append(c)
    print(c)
