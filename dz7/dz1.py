# Напишите функцию print_operation_table(operation, num_rows, num_columns),
# которая принимает в качестве аргумента функцию, вычисляющую элемент
# по номеру строки и столбца.

# Аргументы num_rows и num_columns указывают число строк и столбцов
# таблицы, которые должны быть распечатаны.

# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).

# Если строк меньше двух, выдайте текст
# ОШИБКА! Размерности таблицы должны быть больше 2!.

# Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.

# Пример
# На входе:

# print_operation_table(lambda x, y: x * y, 3, 3)
# На выходе:
x=3
y=3

def operation(num_rows, num_cols):
    for i in range:
        return num_rows*num_cols

# def print_operation_table(operation, num_rows=9, num_columns=9):
#     for i in range(1, num_rows + 1):
#         answer = []
#         for j in range(1, num_columns + 1):
#             answer.append(operation(i, j))
#         print(" ".join(answer))
 
 
# print_operation_table(lambda x, y: x * y)



def print_operation_table(operation, num_rows=x, num_cols=y):
    for x in range(1, num_rows + 1):
        for y in range(1, num_cols + 1):
            if num_cols == y:
                print(operation(x, y))
            else:
                print(operation(x, y), '\t', end='')
                
                
                



def print_operation_table(operation, num_rows=6, num_columns=6):
    a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
    for i in a:
        print(*[f"{x:>3}" for x in i])


print_operation_table(lambda x, y: x * y)






def print_operation_table(operation, num_rows=6, num_columns=6):
    res = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
    for i in res:
        print(*[f"{x}" for x in i])

print_operation_table(lambda x, y: x * y)