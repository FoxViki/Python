def my_lambda(num):
    return num_1 * num_2


f = lambda num_1, num_2: num_1 * num_2
print(f(23,34))

# 11:05
func = lambda x: x ** 2
iter_object = [234,456,78,890,243,546,67]

print(*map(func, iter_object))


map_list = []
for item in iter_object:
    map_list.append(func(item))
    
func_2 = lambda x: x % 2 == 0 
print(*filter(func_2, iter_object))

filter_list = []
for item in iter_object:
    if func_2(item):
        filter_list.append(item)

# №#1) У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине программы используется множество раз и вы не хотите ничего сломать): 

# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))

# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.

# 2) Есть код:

# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#          print(‘ok’)
# else:
#          print(‘fail’)

# - В переменную transformation нужно прописать такую функцию, что бы в переменной transformed_values получилась копия списка values

# 11:20
#
# 
# 11:21
# Яна Краснопольская
trasformation = lambda x: x
values = [1, 23, 42, 'asdfg']
transformed_values = list(map(trasformation, values))
if values == transformed_values:
    print('ok')
else:
    print('fail')