import pandas as pd

# Считываем исходный датасет
df = pd.read_csv("nowcasting_2024-03-11.csv", delimiter=";", encoding="utf-8", header=0)

# Удаляем первый столбец
df.drop(df.columns[0], axis=1, inplace=True)

# Убираем нижнее подчеркивание в названиях столбцов и заменяем его на пробел
df.columns = df.columns.str.replace('_', ' ')

# Убираем кавычки из всех значений строковых столбцов
df = df.applymap(lambda x: x.replace('"', '') if isinstance(x, str) else x)

# Заменяем "-" на "." в столбце "temp"
df['temp'] = df['temp'].str.replace('-', '.')

# Удаляем дефис между датой и временем в столбце "data"
df['data'] = df['data'].str.replace('-', '.')

# Удаляем дефис между датой и временем в столбце "data"
df['wrf_date'] = df['wrf_date'].str.replace('-', '.')


# Удаляем дефис между датой и временем в столбце "data"
df['data'] = df['data'].str.replace('_', ' ')


df['windU'] = df['windU'].str.replace(',', '.')

df['windV'] = df['windV'].str.replace(',', '.')

# Сохраняем измененный датасет в той же папке
df.to_csv("modified_nowcasting_2024-03-11.csv", index=False, sep=';')

print("Измененный датасет сохранен в файл nowcasting_2024-03-08.csv")
