import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Пример синтетических данных (замените своими реальными данными)
data = {
    'Год': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
    'Осадки_зима': [120, 150, 90, 110, 130, 100, 80, 140, 160, 70],
    'Осадки_весна': [200, 180, 220, 240, 170, 210, 190, 230, 250, 160],
    'Осадки_лето': [50, 70, 40, 60, 80, 30, 90, 20, 10, 100],
    'Осадки_осень': [150, 130, 170, 190, 120, 180, 140, 200, 220, 110],
    'Урожайность': [25, 28, 22, 30, 26, 23, 20, 32, 35, 18]
}

df = pd.DataFrame(data)

# Фичи и целевая переменная
X = df[['Осадки_зима', 'Осадки_весна', 'Осадки_лето', 'Осадки_осень']]
y = df['Урожайность']
print(df)
# Разделение на тренировочную и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Создание и обучение модели
model = xgb.XGBRegressor(
    objective='reg:squarederror',
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    random_state=42
)

model.fit(X_train, y_train)

# Прогнозирование
y_pred = model.predict(X_test)

# Метрики
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'MSE: {mse:.2f}')
print(f'R2 Score: {r2:.2f}')

# Визуализация важности признаков
xgb.plot_importance(model)
# plt.show()

# Сравнение реальных и предсказанных значений
results = pd.DataFrame({
    'Реальная урожайность': y_test,
    'Предсказанная урожайность': y_pred
})
print(results)
results.plot(kind='bar', figsize=(10, 6))
plt.title('Сравнение реальной и предсказанной урожайности')
plt.ylabel('Урожайность (т/га)')
plt.show()

# Пример новых данных (осадки за 2020 год)
new_data = pd.DataFrame({
    'Осадки_зима': [130],
    'Осадки_весна': [210],
    'Осадки_лето': [45],
    'Осадки_осень': [175]
})

prediction = model.predict(new_data)
print(f'Прогнозируемая урожайность: {prediction[0]:.1f} т/га')

new_data = pd.DataFrame({
    'Осадки_зима': [130],
    'Осадки_весна': [100],
    'Осадки_лето': [0],
    'Осадки_осень': [100]
})

prediction = model.predict(new_data)
print(f'Прогнозируемая урожайность: {prediction[0]:.1f} т/га')