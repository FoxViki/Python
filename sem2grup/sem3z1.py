# Задача №17. Дан список чисел. Определите, сколько в
# нем встречается различных чисел.

# Input: [1, 1, 2, 0, -1, 3, 4, 4]

# Output: 6


from random import randint


num_list = []
list_length = randint(5, 10)
print(f'{list_length=}')

# for _ in range(list_length):
# new_num = randint(0, 5)
# num_list.append(new_num)

num_list_2 = [randint(0, 5) for _ in range(list_length)]

print(num_list_2)
unique = set(num_list_2)
print(unique)
print(f'{len(unique)=}')


# import random from randint

# list_length = randint(5, 10)
# print(f'{list_length=}')



# num_list_2 = [randint(0, 5) for _ in range(list_length)]
# print(f'{num_list_2=}')

# new_list = []

# for num in num_list_2:
# if num not in new_list:
# new_list.append(num)
# print(f'{new_list=}')

# print(f'{len(new_list)=}')


# # for num in num_list_2:
# # if num in new_list:
# # continue
# # new_list.append(num)