# Задача №1.  За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной
# конструкцией if и циклами.
# Input:
# n = 700км/д
# s= 750км
# Output:
# 2

# import this
#import math # округление вверх вариант 1

# import os
# os.system("cls") очистка консоли

n = int(input('Введите скорость движения автомобиля '))
m = int(input('Введите расстояние '))
#print(math.ceil(m/n)) #вариант 1

print((m+n-1)//n)
# print(m//(-n)*(-1))
# print(m//n + (m%n > 0))


# n = int(input("Введите скорость автомобиля : "))
# m = int(input("Введите необходимое расстоние : "))

# # print(math.ceil(m/n))
# print((m + n-1)//n)

# скорость - 700
# расстояние хотя бы на 1 больше скорости, 
# 1 день - 1 до 700
# 2 день - 701 до 1400
# 3 день - 1401 до 2100

# n-1 = 700 - 1 = 699 //700 = 1
# если m = 701 то  701 +699 = 1400 //700 = 2
# если m = 1400 то 1400 +699 = 2099 // 700 = 2
# если m = 750 то  750 +699 = 1449 // 700 = 2
# print((m + n-1)//n)
#  (n-1)//n =0






