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
# через пробел. Если таких холодильников нет, ничего выводить не нужно.


# Sample Input 1:
# 6
# 222anton456
# a1n1t1o1n1
# 0000a0000n00t00000o000000n
# gylfole
# richard
# ant0n
# Sample Output 1:
# 1 2 3
# Sample Input 2:
# 9
# osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
# anton
# aoooooooooontooooo
# elelelelelelelelelel
# ntoneeee
# tonee
# 253235235a5323352n25235352t253523523235oo235523523523n
# antoooooooooooooooooooooooooooooooooooooooooooooooooooon
# unton
# Sample Output 2:
# 1 2 7 8