# Задача №17. 
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6


#решение
# lst = [1, 1, 2, 0, -1, 3, 4, 4]

# unique = []
# for item in lst:
#     if item not in unique:
#         unique.append(item)

# print(len(unique))

#еще
# nums = [1, 1, 2, 0, -1, 3, 4, 4]

# count = 1
# for i in range(1, len(nums)):
#     if nums[i - 1] != nums[i]:
#         count += 1

# print(count)



# Ирина Лукашова
# numbers = [ 2, 2, 1]
# count = 0
# min = numbers[0]
# numbers1=[]

# for i in numbers:
#     if i not in numbers1:
#         numbers1.append(i)
# print(len(numbers1))

# #второе решение
numbers = [2, 2, 1]

print(len(set(numbers)))
print(set(numbers))


# 3 решение
list_1 = [1, 1, 2, 0, -1, 3, 4, 4]
new_set = set(list_1)
print(list_1)
print(f"В списке {len(new_set)} разных чисел")



# Задача №19. 
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# list = [1, 2, 3, 4, 5]
#k = 3
# Output: [4, 5, 1, 2, 3]

list1 = [1, 2, 3, 4, 5]
k = 7
l = len(list1)
k = k%l

for i in range(k):
    temp = list1.pop()
    list1.insert(0, temp)
    print(list1)
    
    
    
    
    
# второе решение
# l = len(list1)
# k = k%l
# list2 = list1[-k:]+list1[:-k]
# print(list2)



# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

lst = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}] 
lst1 = set()
for i in lst:
    for j,y in i.items():  # валуе значение    итем ключзнаечение   если ничего то ничего.
        print(j,y)
        lst1.add(y)
print (lst1)