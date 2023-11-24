# Напишите функцию, которая принимает одно число и проверяет,
# является ли оно простым

# Напоминание: Простое число - это число, которое имеет 2 делителя:
# 1  и n(само число)


# Input: 5

# Output: yes

def simple_num(number):
    for div in range(2, number):
        if number % div == 0:
            return False
    return True

def num_check(number):
    if number.isdigit() and int(number) > 1:
        return True
    return False

num = input('Enter a number: ')

while not num_check(num):
    print('Incorrect number!')
    num = input('Enter a number: ')

num = int(num)
print('YES' if simple_num(num) else 'NO')




#2 var
def simple_num(number):
    if number % 2 == 0 or number % 3 == 0 and number not in (2,3):
        return False
    for div in range(3, int(number ** 0.5) + 1, 2):
        if number % div == 0:
            return False
    return True

def num_check(number):
    if number.isdigit() and int(number) > 1:
        return True
    return False

num = input('Enter a number: ')

while not num_check(num):
    print('Incorrect number!')
    num = input('Enter a number: ')

num = int(num)
print('YES' if simple_num(num) else 'NO')