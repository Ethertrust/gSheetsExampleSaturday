import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import SimpleExpSmoothing

# Создание временного ряда
dates = pd.date_range(start='2023-01-01', periods=100)
data = np.sin(np.linspace(0, 10, 100)) + np.random.normal(0, 0.2, 100)
ts = pd.Series(data, index=dates)

from prophet import Prophet

# Подготовка данных для Prophet
df = ts.reset_index()
df.columns = ['ds', 'y']

# Создание и обучение модели
model_prophet = Prophet()
model_prophet.fit(df)

# Создание фрейма для прогноза
future = model_prophet.make_future_dataframe(periods=10)
forecast_prophet = model_prophet.predict(future)

# Визуализация
fig = model_prophet.plot(forecast_prophet)
plt.title('Прогнозирование с Prophet')
plt.show()