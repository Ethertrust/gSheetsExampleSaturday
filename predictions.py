import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import SimpleExpSmoothing

# Создание временного ряда
dates = pd.date_range(start='2023-01-01', periods=100)
data = np.sin(np.linspace(0, 10, 100)) + np.random.normal(0, 0.2, 100)
ts = pd.Series(data, index=dates)

from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX

# ARIMA модель
model_arima = ARIMA(ts, order=(2, 1, 1))  # (p, d, q)
results_arima = model_arima.fit()
forecast_arima = results_arima.forecast(steps=10)

# SARIMA модель (с учетом сезонности)
model_sarima = SARIMAX(ts, order=(1, 1, 1), seasonal_order=(1, 1, 1, 7))
results_sarima = model_sarima.fit()
forecast_sarima = results_sarima.forecast(steps=10)

# Визуализация
plt.figure(figsize=(12, 6))
plt.plot(ts, label='Исходный ряд')
plt.plot(forecast_arima, label='ARIMA прогноз', color='red')
plt.plot(forecast_sarima, label='SARIMA прогноз', color='green')
plt.title('Прогнозирование с ARIMA и SARIMA')
plt.legend()
plt.show()