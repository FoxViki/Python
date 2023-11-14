#1. определить с помощью рекурсии, число Х
# является простым

i=2
count=0

def prosto(n,i=2):
    if n==2 or i*i>n:
        return True
    if n%i==0:
        return False
    return prosto(n, i+1)

print(prosto(9))




# i = 2
# count = 0
# def prosto(n, i=2):
# if n ==2 or i *i>n:
# return True
# if n%i ==0:
# return False
# return prosto(n, i+1)

# print(prosto(10))





#2. определить с помощью рекурсии , является ли
# слово полиндромом

def is_palindrom(word):
    if len[word]==word[-(k+1)]:
        print(word)
        return True
    if word[0]==word[-1]:
        print(word)
        return is_palindrom(word[1:-1])
    else:
        return False
word = input()
result= is_palindrom(word.lower())

if result:
    print(f"{word} - палиндром")
else: print(f"{word} - не палиндром")



# def is_palindrome(word):
# if len(word) == 0:
# print(word)
# return True
# if word[0] == word[-1]:
# print(word)
# return is_palindrome(word[1:-1])
# else:
# return False
# word = input("Введите слово: ")
# result = is_palindrome(word.lower())

# if result:
# print(f"{word} - палиндром.")
# else:
# print(f"{word} - не палиндром.")




# Решение в группах
# Два различных натуральных числа n и m
# называются дружественными, если сумма
# делителей числа n (включая 1, но исключая само n)
# равна числу m и наоборот. Например,
# 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k.
# Программа получает на вход одно натуральное
# число k, не превосходящее 105. Программа должна
# вывести все пары дружественных чисел, каждое из
# которых не превосходит k. Пары необходимо выводить
# по одной в строке, разделяя пробелами. Каждая пара
# должна быть выведена только один раз
# (перестановка чисел новую пару не дает).
# Ввод: Вывод:
# 300 220 284
# [(1,1),(2,3)......(220,284)}