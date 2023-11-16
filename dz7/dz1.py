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


# 1 2 3
# 2 4 6 
# 3 6 9
x=3
y=3
num_rows = x
num_columns = y
operation_table=0
def operation_table(num_rows, num_columns):
    return operation_table = num_rows*num_columns
print(i,operation_table)
print_operation_table(lambda x, y: x * y, 3, 3)