#Задача 2: Найдите сумму цифр трехзначного числа. Примеры:
#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0)

#print("Введите трехзначное число")
#n = int(input())
#print (n%10 +(n//10)%10 +(n//100)%10)


#Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
#они сделали S журавликов. Сколько журавликов сделал каждый
#ребенок, если известно, что Петя и Сережа сделали одинаковое
#количество журавликов, а Катя сделала в два раза больше журавликов,
#чем Петя и Сережа вместе?
#Примеры:
#6 -> 1 4 1
#24 -> 4 16 4
#60 -> 10 40 10

#print("Введите число журавликов")
#n = int(input())
#if (n%6 == 0):
#    p = n//6
#    s = p
#    k = p*4
#    print (f"Катя сделала {k}, Петя и Сережа сделали по {p}")
#else:
#    print("Введите число, кратное 6")


#Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
#расплачивались за проезд и получали билет с номером. Счастливым
#билетом называют такой билет с шестизначным номером, где сумма
#первых трех цифр равна сумме последних трех. Т.е. билет с номером
#385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
#программу, которая проверяет счастливость билета.
#Примеры:
#385916 -> yes
#123456 -> no


#Задача 8: Требуется определить, можно ли от шоколадки размером n
#× m долек отломить k долек, если разрешается сделать один разлом по
#прямой между дольками (то есть разломить шоколадку на два
#прямоугольника).
#Примеры:
#3 2 4 -> yes
#3 2 1 -> no