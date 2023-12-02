# Задача №51. Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True, если это так. Если значение характеристики для разных объектов отличается - то False. Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6] same
# if same_by(lambda x: x % 2 == 0, values):
# print(‘same’)
# else:
# print(‘different’)

def same_by_2(characteristics, objects):
res_set = {characteristics(num) for num in objects}
if len(res_set) <= 1:
return True
return False

def same_by_3(characteristics, objects):
result = list(filter(characteristics, objects))
if objects == result or not result:
return True
return False

def same_by_4(characteristics, objects):
result = list(map(characteristics, objects))
if all(result) == any(result):
return True
return False

values = [1, 2, 5, 11]

if same_by_4(lambda x: x % 2 == 0, values):
print('same')
else:
print('different')









var2


def same_by(characteristics, objects):
check_0 = characteristics(objects[0])

for num in objects[1:]:
if check_0 != characteristics(num):
return False

return True


values = [3, 1, 1, 7]

if same_by(lambda x: x % 2 == 0, values):
print('same')
else:
print('different')














































































Виктор Новиков
def sam_by(characteristics, objects):
	count_objects = len(objects)
	res_list = ()
	return count_objects

values = [0, 2, 10, 6]
if same_by(lambda x: x % 2 == 0, values):
	print('same')
else:
	print('different')
 
 
 
 
 
 
 
 
 Задача №51.  Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True, если это так. Если значение характеристики для разных объектов отличается - то False. Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.
Ввод:							Вывод:
values = [0, 2, 10, 6]		same
if same_by(lambda x: x % 2 == 0, values):
	print(‘same’)
else:
	print(‘different’)
 
 
 
 
 
 
 
 
 
 
 def sam_by(characteristics, objects):
	count_objects = len(objects)
	res_list = ()
	return count_objects

values = [0, 2, 10, 6]
if same_by(lambda x: x % 2 == 0, values):
	print('same')
else:
	print('different')
 
 
 
 
 
 
 
 
 
 
 
 
 
 def same_by_3(characteristics, objects):
    result = list(filter(characteristics, objects))
    if len(result) != 0:
        return False
    else:
        return True
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def same_by(characteristics, objects):
    check_0 = characteristics(objects[0])
      
    for num in objects[1:]:
        if check_0 != characteristics(num):
            return False
        
    return True    
              

values = [3, 1, 1, 7]

if same_by(lambda x: x % 2 == 0, values):
    print('same')
else:
    print('different')
    
    
    
    
    
    
    
    
    
    def same_by(characteristic, objects):
    res_list = set()
    for item in objects:
        res_list.add(characteristic(item))
    if len(res_list) < 1:
        return True
    else:
        return False

13:01
def same_by(characteristic, objects):
    res_list = set()
    for item in objects:
        res_list.add(characteristic(item))
    if len(res_list) <= 1:
        return True
    else:
        return False
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def same_by_3(characteristics, objects):
    result = list(filter(characteristics, objects))
    if len(result) != 0:
        return False
    else:
        return True
    
    
    
    
    
    
    
    
    print(all([True, True, True, True]))
print(all([True, False, True, True]))
print(all([False, False, False, False]))
print()
print(any([True, True, True, True]))
print(any([True, False, True, True]))
print(any([False, False, False, False]))
print()
print(all([1, 2, 3, 4]))
print(all([1, 0, 3, 4]))
print(all([0, 0, 0, 0]))
print()
print(any([1, 2, 3, 4]))
print(any([1, 0, 3, 4]))
print(any([0, 0, 0, 0]))
print()
print(all(['dfg', 'sdf', 'sdf', 'cvb']))
print(all(['dfg', '', 'sdf', 'cvb']))
print(all(['', '', '', '']))
print()
print(any(['dfg', 'sdf', 'sdf', 'cvb']))
print(any(['dfg', '', 'sdf', 'cvb']))
print(any(['', '', '', '']))
print()
print(all([[''], ('',), {''}, ['']]))
print(all([[''], [], [''], ['']]))
print(all([{}, {}, {}, []]))
print()
print(any([[''], ('',), {''}, ['']]))
print(any([[''], [], [''], ['']]))
print(any([{}, {}, {}, []]))







def same_by_3(characteristics, objects):
    result = list(filter(characteristics, objects))
    print(*result)
    if len(result) != 0:
        return False
    else:
        return True
    
    
    
    
   
   
    









print(all([True, True, True, True]))
print(all([True, False, True, True]))
print(all([False, False, False, False]))
print()
print(any([True, True, True, True]))
print(any([True, False, True, True]))
print(any([False, False, False, False]))
print()
print(all([1, 2, 3, 4]))
print(all([1, 0, 3, 4]))
print(all([0, 0, 0, 0]))
print()
print(any([1, 2, 3, 4]))
print(any([1, 0, 3, 4]))
print(any([0, 0, 0, 0]))
print()
print(all(['dfg', 'sdf', 'sdf', 'cvb']))
print(all(['dfg', '', 'sdf', 'cvb']))
print(all(['', '', '', '']))
print()
print(any(['dfg', 'sdf', 'sdf', 'cvb']))
print(any(['dfg', '', 'sdf', 'cvb']))
print(any(['', '', '', '']))
print()
print(all([[''], ('',), {''}, ['']]))
print(all([[''], [], [''], ['']]))
print(all([{}, {}, {}, []]))
print()
print(any([[''], ('',), {''}, ['']]))
print(any([[''], [], [''], ['']]))
print(any([{}, {}, {}, []]))
print()
Денис Апрышко def same_by_3(characteristics, objects):
result = list(filter(characteristics, objects))
print(*result)
if len(result) != 0:
return False
else:
return True    