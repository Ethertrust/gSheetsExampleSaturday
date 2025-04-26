import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import SimpleExpSmoothing

# Создание временного ряда
dates = pd.date_range(start='2023-01-01', periods=100)
data = np.sin(np.linspace(0, 10, 100)) + np.random.normal(0, 0.2, 100)
ts = pd.Series(data, index=dates)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

# Нормализация данных
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(ts.values.reshape(-1, 1))

# Подготовка данных для LSTM
def create_dataset(data, look_back=1):
    X, y = [], []
    for i in range(len(data)-look_back-1):
        X.append(data[i:(i+look_back), 0])
        y.append(data[i+look_back, 0])
    return np.array(X), np.array(y)

look_back = 5
X, y = create_dataset(scaled_data, look_back)
X = np.reshape(X, (X.shape[0], X.shape[1], 1))

# Создание модели LSTM
model_lstm = Sequential()
model_lstm.add(LSTM(50, return_sequences=True, input_shape=(look_back, 1)))
model_lstm.add(LSTM(50))
model_lstm.add(Dense(1))
model_lstm.compile(loss='mean_squared_error', optimizer='adam')
model_lstm.fit(X, y, epochs=10, batch_size=1, verbose=1)

# Прогнозирование
inputs = scaled_data[-look_back:]
forecast_lstm = []
for _ in range(10):
    x_input = inputs.reshape((1, look_back, 1))
    y_pred = model_lstm.predict(x_input, verbose=0)
    forecast_lstm.append(y_pred[0,0])
    inputs = np.append(inputs[1:], y_pred)

# Обратное преобразование данных
forecast_lstm = scaler.inverse_transform(np.array(forecast_lstm).reshape(-1, 1))

# Визуализация
plt.figure(figsize=(12, 6))
plt.plot(ts, label='Исходный ряд')
plt.plot(pd.date_range(ts.index[-1], periods=11)[1:], forecast_lstm,
         label='LSTM прогноз', color='red')
plt.title('Прогнозирование с LSTM')
plt.legend()
plt.show()