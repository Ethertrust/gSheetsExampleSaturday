import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from xgboost import XGBRegressor

# Создание временного ряда
dates = pd.date_range(start='2023-01-01', periods=100)
data = np.sin(np.linspace(0, 10, 100)) + np.random.normal(0, 0.2, 100)
ts = pd.Series(data, index=dates)

# Создание признаков для временного ряда
def create_features(df):
    df['day'] = df.index.day
    df['month'] = df.index.month
    df['dayofweek'] = df.index.dayofweek
    df['dayofyear'] = df.index.dayofyear
    return df

df = ts.to_frame(name='value')
df = create_features(df)

# Разделение на обучающую и тестовую выборки
train = df.iloc[:-10]
test = df.iloc[-10:]

# Определение признаков и целевой переменной
features = ['day', 'month', 'dayofweek', 'dayofyear']
X_train, y_train = train[features], train['value']
X_test, y_test = test[features], test['value']

# Обучение модели
model_xgb = XGBRegressor(n_estimators=100, learning_rate=0.1)
model_xgb.fit(X_train, y_train)

# Прогнозирование
forecast_xgb = model_xgb.predict(X_test)

# Визуализация
plt.figure(figsize=(12, 6))
plt.plot(ts, label='Исходный ряд')
plt.plot(test.index, forecast_xgb, label='XGBoost прогноз', color='red')
plt.title('Прогнозирование с XGBoost')
plt.legend()
plt.show()