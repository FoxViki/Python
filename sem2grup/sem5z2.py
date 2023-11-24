# Задача №33. Хакер Василий получил доступ к классному
# журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия,
# но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4

# Output: 1 3 3 3 1
from random import randint
import time
n = randint(5,15)
list1 = [randint(1,5) for _ in range(n)]
print(list1)

start_time = time.time()
min_num = min(list1)
max_num = max(list1)

for i in range(len(list1)):
    if list1[i] == max_num:
        list1[i] = min_num
print(list1)

end_time = time.time()
print(end_time - start_time)

#2 variant
from random import randint
import time

n = randint(5,15)
list1 = [randint(1,5) for _ in range(n)]
print(list1)

start_time = time.time()

min_num = list1[0]
max_num = list1[0]
list_max_num = [0]

for i in range(1, len(list1)):
    if list1[i] > max_num:
        max_num = list1[i]
        list_max_num = [i]
    elif list1[i] == max_num:
        list_max_num.append(i)
    if list1[i]<min_num:
        min_num=list1[i]
        
for i in list_max_num:
    list1[i]=min_num
    
print(list1)

end_time = time.time()
print(end_time - start_time)