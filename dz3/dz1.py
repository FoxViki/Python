# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел A.
# . Последняя строка содержит число X

list_1 = [1, 3, 2, 3, 3, 4, 5]
k = 3
count = 0

for i in list_1:
    if i == k:
        count += 1
print(count)

# или 
#print(list_1.count(k))

