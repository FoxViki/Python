# Дано натуральное число A > 1. Определите,
# каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите число -1.
# Input:     5
# Output:  6

a = input("Input a number: ")

while not a.isdigit() or a == "0" or a == "1":
    print("Error input")
    a = input("Input a number: ")

a = int(a)

pos = 3
pred = 1
pred2 = 1
while pred < a:
    pred, pred2 = pred + pred2, pred     #множественное присваивание одновременно
    pos += 1

if pred != a:
    print(-1)
else:
    print(pos)
    
    
    
    
    
    
#     fjgfcfchcmghvv,gvv
# pos = 3
# pred = 1
# pred2 = 1
# while pred < a:
#     temp=pred
#     pred= pred + pred2
#     pred2=temp
#     pos += 1