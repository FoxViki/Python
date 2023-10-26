# Задача No25.
# Напишите программу, которая принимает на вход строку,
# и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью
# постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

# string_input = 'a a a b c a a d c d d'.split()
# print(string_input)
# dict_result = {}
# for i in string_input:
#     if i not in dict_result:
#         # dict_result[i]=0
#         print(i, end=' ')
#     else:
#         # dict_result[i]+=1
#         print(f'{i}_{dict_result[i]}', end=' ')
#     dict_result[i]=dict_result.get(i, 0)+1        это метод гет тогда коментим дист в ифе выше



# Задача No27.
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов. Определите,
# сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that
# she sells are sea shells I'm sure.So if she sells sea shells
# on the sea shore I'm sure that the shells are sea shore shells
# Output: 13

# text1 = '''She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells'''
# n = text1.replace('.', ' ').replace('\n', ' ').lower().split(' ')
# a = set(n)
# print(len(a))
# print(a)

# # или
# input_str = '''She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells'''.replace("\'",' ').replace(".",' ').upper().split()
# print(input_str,len(set(input_str)))


# задача про холольник
# Искусственный интеллект Антон, созданный Гилфойлом,
# взломал сеть умных холодильников. Теперь он использует их
# в качестве серверов "Пегого дудочника". Помогите владельцу
# фирмы отыскать все зараженные холодильники.

# Для каждого холодильника существует строка с данными,
# состоящая из строчных букв и цифр, и если в ней присутствует
# слово "anton" (необязательно рядом стоящие буквы, главное
#                наличие последовательности букв), то
# холодильник заражен и нужно вывести номер холодильника,
# нумерация начинается с единицы
# Формат входных данных
# В первой строке подаётся число 
# n
# n – количество холодильников. В последующих 
# n
# n строках вводятся строки, содержащие латинские строчные
# буквы и цифры, в каждой строке от 
# 5
# 5 до 
# 100
# 100 символов.

# Формат выходных данных
# Программа должна вывести номера зараженных холодильников
# через пробел. Если таких холодильников нет, ничего
# выводить не нужно.



# s1 = '6'
# s2 = '222anton456'
# s3 = 'a1n1t1o1n1'
# s4 = '0000a0000n00t00000o000000n'
# s5 = 'gylfole'
# s6 = 'richard'
# s7 = 'ant0n'
# s8 = '9'
# s9 = 'osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen'
# s10 = 'c'
# s11 = 'aoooooooooontooooo'
# s12 = 'elelelelelelelelelel'
# s13 = 'ntoneeee'
# s14 = 'tonee'
# s15 = '253235235a5323352n25235352t253523523235oo235523523523n'
# s16 = 'antoooooooooooooooooooooooooooooooooooooooooooooooooooon'
# s17 = 'unton'

# k = 'anton'
# s = k.split()

# dict = {s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17}
# for i in s:
#     a = 0
#     n = 0
#     t = 0
#     o = 0
#     n = 0
#     for j in dict:
#         if j == 'a':
#             a == True
#             y = j
#             if a == True & i == 'n':
#                 n == True
#                 if a == True & n == True & i == 't':
#                     t == True
#                     if a == True & n == True & t == True & i == 't':
#                         o == True
#                         if a == True & n == True & t == True & o == True & i == 't':
#                             n == True
#                             print('Заражен')
#     print(f'Заражен этот холодидьник {dict[j]}')
                        
        
#         print("Найден вирус 'anton' at position", position)
#     else:
#         print("Вирусов нет", position)
#     dict = dict.upper()
    
    
     
# r=[] #список с номерами результатов
# n = int(input()) 
# for i in range(n):
#     a,n,t,o,nn=0,0,0,0,0 #устанавливаем что все буквы не найдены
#     s = str(input()) 
#     for j in s:
#        if j =='a':
#             a = True
#        if j='n' and a: #если найдена буква n и до этого была найдена буква а
#              n=True #то помечаем букву n как найденую
#        if j='t' and n:
#               t=True
#        if j='o' and t:
#              o=True
#        if j='n' and o: #если найдена последняя буква n
#              r.append(i) #добавляем номер в список результатов
#               print('virus') 
#               break; #завершаем поиск по строке, так как цель достигнута
# if res == 'anton':
#         print(i, end=' ')
        
        
        
        
        
        
        
        
# верное решение Никита Шаров
# virus = 'anton'
# n = int(input('Введите кол-во холодильников: '))
# infected_fridges = []

# for i in range(n):
#     code_fridge = (input(f'Введите код {i + 1} холодильника: '))

#     index = 0
#     found = False
#     for letter in code_fridge:
#         if letter == virus[index]:
#             index += 1
#         if index == len(virus):
#             found = True
#             break
#     if found:
#         infected_fridges.append(i + 1)
# print(infected_fridges) держи моё но оно другое