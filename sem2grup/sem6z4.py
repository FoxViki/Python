# 45.Два различных натуральных числа n и m называются дружественными,
# если сумма делителей числа n (включая 1, но исключая само n)
# равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из
# которых не превосходит k. Программа получает на вход одно
# натуральное число k, не превосходящее 105. Программа должна
# вывести  все пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в строке,
# разделяя пробелами. Каждая пара должна быть выведена только
# один раз (перестановка чисел новую пару не дает).
# Ввод:			Вывод:
# 300			220 284

# def get_sum_div(num):
#     sum_div = 1
#     for div in range(2, num):
#         if num % div == 0:
#             sum_div += div
#     return sum_div


# def chec_friend_num(number):
#     for first_num in range(2, number):
#         second_num = get_sum_div(first_num)
#         if first_num < second_num and get_sum_div(second_num) == first_num:
#             print(first_num, second_num)


# k = int(input("Введите число: "))
# chec_friend_num(k)



# var2

def get_sum_div(num):
    sum_div = 1
    sqrt_num = int(num**0.5)
    for div in range(2, sqrt_num):
        if num % div == 0:
            sum_div += div + num//div
    if sqrt_num == num**0.5:
        sum_div += sqrt_num
    return sum_div


def chec_friend_num(number):
    for first_num in range(2, number):
        second_num = get_sum_div(first_num)
        if first_num < second_num and get_sum_div(second_num) == first_num:
            print(first_num, second_num)


k = int(input("Введите число: "))
chec_friend_num(k)
