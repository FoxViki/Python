# Задача №43.  Дан список чисел. Посчитайте, сколько в
# нем пар элементов, равных друг другу. Считается, что
# любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список чисел.
# Все числа списка находятся на разных строках.

# 2) (пользовательский ввод можно заменить на рандомный)
# Пользователь вводит  размер массива – N
# и элементы массива (целые числа). 
# нужно посчитать сколько повторений у каждого числа
# посчитанные числа можно посчитать повторно в паре с другими числами

# Ввод:			Вывод:
# 1 2 3 2 3 2			4

arr_size = int(input('Введите размер массива: '))
arr_new = [randint(0, 5) for _ in range(arr_size)]
print(arr_new)

#1
count = 0
for i in range(arr_size - 1):
    for j in range(i + 1, arr_size):
        if arr_new[i] == arr_new[j]:
            count += 1
            
print(count)


#2
count = 0
for num in set(arr_new):
    count_num = arr_new.count(num)
    count += count_num * (count_num - 1) // 2
    
print(count)