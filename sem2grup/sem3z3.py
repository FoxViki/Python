# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}


list_dicts = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
{"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]

my_set = set()

for curr_dict in list_dicts:
    for val in curr_dict.values():
        my_set.add(val)
print(my_set)

#var3
# my_set = set()

# for curr_dict in list_dicts:
#     my_set.add(*curr_dict.values()):   *-выковыривает один только обьект внутри. если два обьекта то не прет
# если много значений то используетс строка с ф-ей update-она как распаковка: my_set.update(curr_dict.values()):
# print(my_set)





# for curr_dict in list_dicts:
#     for val in curr_dict.values():
#         my_set.add(val.strip()) стрип удаляет пробелы. и один элемент уйдет еще
# print(my_set)




# def unique_values(dictionary_list):
# return {value for d in dictionary_list for value in d.values()}

# input_list = [
# {"V": "S001"},
# {"V": "S002"},
# {"VI": "S001"},
# {"VI": "S005"},
# {"VII": "S005"},
# {"V": "S009"},
# {"VIII": "S007"}
# ]

# output = unique_values(input_list)
# print(output)