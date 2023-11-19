# num_rows=3
# num_columns=3
# x=num_rows
# y=num_columns
  
      
      
        
# def print_operation_table(operation, num_rows=x, num_columns=y):
#     rez = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
#     if x<2: print('ОШИБКА! Размерности таблицы должны быть больше 2!')
#     else:
#         for i in rez:
#             print(*[f"{x}" for x in i])

# print_operation_table(lambda x, y: x * y)
x=3
y=3
num_rows=x
num_columns=y


def operation(x,y):
    z = x*y
    print(z)
    
    
def print_operation_table(operation, num_rows, num_columns):
    if x<2: print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        for i in range(1, num_rows + 1):
            for j in range(1, num_columns + 1):
                a = operation(i, j)
                print(a)
       

print_operation_table(lambda x, y: x * y, num_rows, num_columns)