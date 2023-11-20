# планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits),
# которая среди списка орбит планет найдет ту, по которой вращается
# самая далекая планета. Круговые орбиты не учитывайте: вы знаете,
# что у вашей звезды таких планет нет, зато искусственные спутники 
# были были запущены на круговые орбиты. Результатом функции должен 
# быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой 
# планеты. Каждая орбита представляет из себя кортеж из пары 
# чисел - полуосей ее эллипса. Площадь эллипса вычисляется
# по формуле S = pi*a*b, где a и b - длины полуосей эллипса. 
# При решении задачи используйте списочные выражения. 
# Подсказка: проще всего будет найти эллипс в два шага: сначала 
# вычислить самую большую площадь эллипса, а затем найти и сам 
# эллипс, имеющий такую площадь. Гарантируется, что самая далекая 
# планета ровно одна
# Пример ввода и вывода данных представлены на следующем слайде
# Задача No49. Решение в группах
# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10

import math
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
ellipse_square=lambda a,b: math.pi*a*b
# print(ellipse_square(7,2))
find_max_far_orbit=lambda lst_orbits: max([ellipse_square(*i) for i in lst_orbits if len(set(i))!=1])
find_farthest_orbit_params=lambda lst_orbits: lst_orbits[[ellipse_square(*i) for i in lst_orbits].index(find_max_far_orbit(lst_orbits))]
print(*find_farthest_orbit_params(orbits))


# Краткое решение:
print(max(orbits,key=lambda x: x[0]*x[1]*(x[0]!=x[1])))









# С помощью лямбда ф-й определить является ли число х двузначным числом.

number = int(input("Введите число: "))
is_two_digit = lambda x: 10 <= x <= 99
result = is_two_digit(number)
print(f"Число {number} является двузначным: {result}")





# С помощью лямбда ф-й определить является какие числа х
# двузначным числом.8 11 0 -23 140 1 => 11 -23
num = '8 11 0 -23 140 1'
print(*filter(lambda x: 10<= abs(int(x))<= 99, num.split()))

var2

print(*filter(lambda x: len(str(abs(int(x))))==2, num.split()))


