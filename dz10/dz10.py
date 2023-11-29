import random

import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst) # перемешивание
print(lst)

data = pd.DataFrame({'whoAmI':lst})
data.loc[data['whoAmI'] == 'robot', 'robot_group'] = '1'
data.loc[data['whoAmI'] != 'robot', 'robot_group'] = '0'
data.loc[data['whoAmI'] == 'human', 'human_group'] = '1'
data.loc[data['whoAmI'] != 'human', 'human_group'] = '0'

data.head(n=20) 
data.drop(columns='whoAmI')#удаление столбца