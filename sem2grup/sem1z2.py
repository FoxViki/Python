# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты
# для них новыми партами. За каждой партой может
# сидеть два учащихся. Известно количество учащихся
# в каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

x = int(input('Qty of student in 1.class: '))
y = int(input('Qty of student in 2.class: '))
z = int(input('Qty of student in 3.class: '))

print(f"It is required to buy {(-(-x//2)-(-y//2)-(-z//2))} scool desks")
print(f"It is required to buy {(x+1)//2+ (y+1)//2+ (z+1)//2} scool desks")

