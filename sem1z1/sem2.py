# Задача 9. По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * ... * N (произведение
# всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
# Input: 5
# Output: 120

n = int(input("Введите целое неотрицательное число n: "))
result = 1
i = 1

while i <= n:
    result *= i
    i += 1

print(f"{n}! = {result}")


# или 
# result = 1
# num = 5

# if (num == 0):
#     print (1)
# else:
#     while(num > 0):
#         result *= num
#         num += 1
#         print (num)
# print(num)

n0 = 0 # n-2 элемент
n1 = 1 # n-1 элемент
n = 1 # n = (n-2)+(n-1)
count = 1
res = 0
while (res<n):
    res = n0+n1
    n0 = n1
    n1 = res
    count += 1
#print(res)
if res==n:
    print(count)
else:
    print(-1)

# Задача 11. Дано натуральное число A > 1. Определите,
# каким по счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не является
# числом Фибоначчи, выведите число -1.
# Input: 5 Output: 6


# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи
# оно является, то есть выведите такое число n, что φ(n)=A. Если А не является
# числом Фибоначчи, выведите число -1.

A = int(input("Введите натуральное число A:"))
prev = 0
curr = 1
n = 1

while curr < A:
    temp = curr
    curr += prev
    prev = temp
    n += 1

if curr == A:
    print("Число", A, "является", n, "-м числом Фибоначчи.")
else:
    print("Число", A, "не является числом Фибоначчи, выводим -1.")