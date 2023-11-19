# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
import random; from randint

#var1
k = 4
new_list = [randint(0, 5) for _ in range(randint(5, 10))]
print(new_list)
# res_list = new_list[-k:] + new_list[:-k]
# print(res_list)




#var2#
# for shift in range(k):
#     shifter_num = new_list.pop()
#     new_list.insert(0, shifter_num)
# print(new_list)

#var1
# k = 4
# new_list = [randint(0, 5) for _ in range(randint(5, 10))]
# print(new_list)
# # res_list = new_list[-k:] + new_list[:-k]
# print(res_list)




#var2
# for shift in range(k):
#     shifter_num = new_list.pop()
#     new_list.insert(0, shifter_num)
# print(new_list)