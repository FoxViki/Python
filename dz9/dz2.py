# импортируем пандас
import pandas as pd

df = pd.read_csv('california_housing_train.csv')# читаем файл
# Находим инимальное значение 'population'
min_population = df['population'].min()

# Выбираем строки 'population' минимальные по значению и ищем максимальное значение 'households' с этих строках
max_households_in_min_population = df[df['population'] == min_population]['households'].max()