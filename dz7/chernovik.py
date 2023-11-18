num_rows=3
num_columns=3
x=num_rows
y=num_columns
  
      
      
        
def print_operation_table(operation, num_rows=x, num_columns=y):
    rez = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
    if x<2: print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        for i in rez:
            print(*[f"{x}" for x in i])

print_operation_table(lambda x, y: x * y)