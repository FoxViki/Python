#импортируем пандас
import pandas as pd

df = pd.read_csv('california_housing_train.csv')#читаем файл
#при условии размера популяции ищем медиальное значение медианхаусавалуе
avg = df[(df['population'] > 0) & (df['population'] < 500)]['median_house_value'].mean()  