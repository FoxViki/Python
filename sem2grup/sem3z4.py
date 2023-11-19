# Задача №23. Дан массив, состоящий из целых чисел.
# Напишите программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента с предыдущим номером)

# Input: [0, -1, 5, 2, 3]

# Output: 2
# Пояснение: (-1 < 5, 2 < 3)

# Примечание: Пользователь может вводить значения списка
# или список задан изначально.

data_list = [0, -1, 5, 2, 3]
count = 0

for i in range(len(data_list)-1):
    if data_list[i] < data_list[i+1]:
        count += 1

print(f'{count=}')
# var2
# new_list = [1 for i in range(len(data_list)-1) if data_list[i] < data_list[i+1]]
# print(sum(new_list))
# var3
# new_list = [1 if data_list[i] < data_list[i+1] else 0 for i in range(len(data_list)-1)]
# print(sum(new_list)) это форма написания если есть элс вместе с ифом







# dopolnenie


# Николай Мануилов my_dict = {'Иванов':1, 'Петров': 2, 'Сидоров':3, 'Николаев':4}
# # print(f'{my_dict=}')
# # print(f'{my_dict["Петров"]=}')
# # print()
# # print(f'{len(my_dict.keys())=}')
# # print(f'{sum(my_dict.values())=}')
# # print(f'{my_dict.items()=}')
# # print()
# # print(f'{list(my_dict.keys())[3]=}')
# # print(f'{list(my_dict.values())=}')
# # print(f'{list(my_dict.items())=}')
# # print()

# # for key in my_dict:
# # print(key, end='\t')
# # print('\n')

# # for key in my_dict.keys():
# # print(key, end='\t')
# # print('\n')

# # for value in my_dict.values():
# # print(value, end='\t')
# # print('\n')

# # for item in my_dict.items():
# # print(item, end='\t')
# # print('\n')

# # q,w,*e = (111,222)
# # print(q)
# # print(w)
# # print(e)

# # my_list = [(1,2,3), (11,22,33), (111,222,333)]
# # for q,w,*e in my_list:
# # print(q, w, e, sep='-')

# for key, value in my_dict.items():
# print(key,value, sep=': ', end='\t')
# print('\n')