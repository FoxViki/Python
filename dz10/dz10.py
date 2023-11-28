import random

import pandas as pd

lst = ['robot'] * 10 #создадим 20 строк со значениями в перемешенном порядке
lst += ['human'] * 10 #получится одна колонка
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
# надо создать 2 столбца по 20 строк и в них 0 и 1.
data = pd.DataFrame({'robot':lst*10}{'human':lst*10})
data.head()
while i in df[{'whoAmI':lst[i]}]:
    if {'whoAmI':lst[i]}==['robot']:
        {'robot':lst[i]}=1
        {'human':lst[i]}=0

# import pandas as pd

# def create_data_frame():
#     data = {'whoAmI': ['robot'] * 10 + ['human'] * 10}
#     return pd.DataFrame(data)

# def main():
#     data = create_data_frame()
#     print(data.head())

# if name == 'main':
#     main()






def create_one_hot_encoder(n, m):
    result = []
    for _ in range(n):
        row = [0] * m
        for col in range(m):
            if col == 0:
                row[col] = 1 if _ % 2 == 0 else 0
            else:
                row[col] = 0 if _ == 0 else 1
        result.append(row)
    return result

n = 20
m = 2
result = create_one_hot_encoder(n, m)

for row in result:
    print(row)
Ответь иначе
Хороший ответ
Плохой ответ
Справка





import pandas as pd

data = {'robot': ['0', '1'], 'human': ['1', '0']}
df = pd.DataFrame(data)
print(df)








import pandas as pd
from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder() # создаем объект encoder
data = enc.fit_transform(data['whoAmI'].values.reshape(-1, 1)) # применяем его к данным
pd.DataFrame(data, columns=enc.categories_) # создаем фрейм данных   