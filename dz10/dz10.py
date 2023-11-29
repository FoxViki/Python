import random

import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst) # перемешивание
print(lst)

data = pd.DataFrame({'whoAmI':lst})#добавляем колонки и выводим значения в ячейки на пересечении хуайэма и колонки
data.loc[data['whoAmI'] == 'robot', 'robot_str'] = '1'
data.loc[data['whoAmI'] != 'robot', 'robot_str'] = '0'
data.loc[data['whoAmI'] == 'human', 'human_str'] = '1'
data.loc[data['whoAmI'] != 'human', 'human_str'] = '0'

data.head(n=20) 
data.drop(columns='whoAmI')#удаление столбца хуайэм