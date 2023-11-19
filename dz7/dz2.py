# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу.

# Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе
# несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами.

# Стихотворение  Винни-Пух передаст вам автоматически в
# переменную stroka в виде строки. В ответе напишите
# Парам пам-пам, если с ритмом все в порядке и Пам парам,
# если с ритмом все не в порядке.
# Если фраза только одна, то ритм определить не получится
# и необходимо вывести: Количество фраз должно быть больше одной!.

# Пример

# На входе:

stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# stroka = 'за-гад-ка-ра-свет-ка-ра-газ-да-не-на-ма-ли-ва-ла'

def rhythm(stroka):
    fraza = stroka.split()

    if len(fraza)<=1:
        return "Количество фраз должно быть больше одной!"
    
    def count_sum_glas(slovo):
        glas = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'
        sum_glas = 0
        for i in slovo:
            if i in glas:
                sum_glas +=1
        return sum_glas
    
    glas_counts = [count_sum_glas(slovo.replace('-', '')) for slovo in fraza]
    
    
    if all(count == glas_counts[0] for count in glas_counts):
        return "Парам пам-пам"
    else:
        return "Пам парам"

result = rhythm(stroka)
print(result) 
     
 







# def check_rhythm(pooh_poetry):
#     phrases = pooh_poetry.split()

#     # Проверяем, что количество фраз больше одной
#     if len(phrases) <= 1:
#         return "Количество фраз должно быть больше одной!"

#     # Функция для подсчета слогов (гласных) в слове
#     def count_syllables(word):
#         vowels = "уеыаоэяиюУЕЫАОЭЯИЮ"
#         return sum(1 for char in word if char in vowels)

#     # Получаем количество слогов в каждой фразе
#     syllables_counts = [count_syllables(phrase.replace('-', '')) for phrase in phrases]

#     # Проверяем, что количество слогов одинаковое в каждой фразе
#     if all(count == syllables_counts[0] for count in syllables_counts):
#         return "Парам пам-пам"
#     else:
#         return "Пам парам"

# result = check_rhythm(stroka)
# print(result)




















































# def proverka(a):
#     a = a.split()
#     l = len(a)
#     if l==1:
#         print("Количество фраз должно быть больше одной!")
#         return True
# if proverka != True:
# if rhythm(stroka):
#     print("Парам пам-пам")
# else:
#     print("Пам парам")

       
    
        
    
# def check_rhythm(pooh_poetry):
#     phrases = pooh_poetry.split()

#     # Проверяем, что количество фраз больше одной
#     if len(phrases) <= 1:
#         return "Количество фраз должно быть больше одной!"

#     # Функция для подсчета слогов (гласных) в слове
#     def count_syllables(word):
#         vowels = "уеыаоэяиюУЕЫАОЭЯИЮ"
#         return sum(1 for char in word if char in vowels)

#     # Получаем количество слогов в каждой фразе
#     syllables_counts = [count_syllables(phrase.replace('-', '')) for phrase in phrases]

#     # Проверяем, что количество слогов одинаковое в каждой фразе
#     if all(count == syllables_counts[0] for count in syllables_counts):
#         return "Парам пам-пам"
#     else:
#         return "Пам парам"

# result = check_rhythm(stroka)
# print(result)
    
    
    
    
    
    
    
    
    
       
#               sum +=1
#         # count_glasnye = sum(1 for bukva in slova[0] if bukva in glasnye)
    
#         for phrase in slova:
        
#             if sum(1 for bukva in phrase if bukva in glasnye) != count_glasnye:
#                 return 'Пам парам'
    
#         return 'Парам пам-пам'

# print(rhythm(stroka))






# stroka = 'за-гад-ка-ра-свет-ка-ра-газ-да-не-на-ма-ли-ва-ла'

# stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# # На выходе:
# # Парам пам-пам

# def rhythm(stroka):
#     slova = stroka.split()
#     glasnye = 'аеёиоуыэюя'
#     print(slova)
    
#     count_glasnye = sum(1 for char in slova[0] if char in glasnye)
    
#     for phrase in slova:
        
#         if sum(1 for char in phrase if char in glasnye) != count_glasnye:
#             return 'Пам парам'
    
#     return 'Парам пам-пам'

# str_1 = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# print(rhythm(str_1))






# def rhythm(poem):
#     poem = poem.split()
#     f = lambda word: sum(1 for i in word if i in 'аеёиоуыэюя')
#     sum_word = f(poem[0])
#     return all([f(i) == sum_word for i in poem])

# poem = str(input("Введите стихотворение: "))

# if rhythm(poem):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')





# stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'

# kolvofras=len(stroka)
# print(kolvofras)
# if kolvofras == 1:
#     print("Количество фраз должно быть больше одной!")        
# else:
#     print()

# def summa_gl(slova):
#     glasnye = 'аеёиоуыэюя'
#     sum_gl=0
#     for bukva in slova:
#         count_glasnye=0
#         if bukva in glasnye:
#             count_glasnye = 1
#             sum_gl +=1
#         else: count_glasnye = 0
#     return sum_gl

    
    
    
    
#     count_glasnye = sum(1 for char in slova[0] if char in glasnye)
#     if sum(1 for char in phrase if char in glasnye) != count_glasnye:
#             return 'Пам парам'
    
#     return 'Парам пам-пам'