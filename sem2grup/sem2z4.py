# Задача №15. 1) Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей,
# а для тещи полегче. Но вот незадача: арбузов слишком
# много и он не знает как же выбрать самый легкий и самый
# тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов.
# Вторая строка содержит N чисел, записанных на новой строчке каждое.
# Здесь каждое число – это масса соответствующего арбуза
# 2) Пользователь вводит одно число N.  Далее идут N чисел,
# записанных на новой строчке каждое. Вывести максимальное и минимальное (циклы)
# Input:	5 -> 5 1 6 5 9


# num = int(input('Enter a number: '))
# min_weight = 1000
# max_weight = 0

# for _ in range(num):
#     weight = int(input('Enter a number: ', end=' '))
    
#     if weight > max_weight:
#         max_weight = weight
        
#     if weight < min_weight:
#         min_weight = weight
        
# print()       
# print(min_weight, max_weight)



#2
from random import randint

num = randint(1, 20)
weight = randint(5, 15)#рандом одного арбуза
print(weight, end=' ')
min_weight = weight
max_weight = weight

for _ in range(num - 1):
    weight = randint(5, 15)#рандом остальные арбузи и поэтому num-1
    print(weight, end=' ')
    max_weight = max(max_weight, weight)
    min_weight = min(min_weight, weight)

print()    
print(min_weight, max_weight)







# допзадачи
# # range(start=0, stop, step=1)

# # range(5) # range(start=0, 5, step=1) -> 0, 1, 2, 3, 4 
# # range(2, 5) # range(2, 5, step=1) -> 2, 3, 4 
# # range(2, 12, 2) # range(2, 12, 2) -> 2, 4, 6, 8, 10 

# text = 'sdfsdgcgnd sdfghert sxfgery ert'
# # print(*range(len(text)))
# # print(list(range(len(text))))
# # for i in range(len(text)):
# #     print(i, text[i], sep=' - ')
    
# # print()
# # for symbol in text:
# #     print(symbol, end='')
    
    
# for i in range(len(text)):
#     if i % 3 == 0:
#         continue
#     if text[i] == 'f':
#         break
#     print(i, text[i], sep=' - ')
# else:
#     print('Мы прошлись по всей строке полностью')


# n = 1    
# while True:
#     print('Бесконечный цикл')
#     n +=1 
#     if n % 5 == 0:
#         break
    
# n = 1    
# while n % 5 != 0:
#     n +=1