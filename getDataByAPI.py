import requests
import pandas as pd

url = "https://data.admhmao.ru/api/data/index.php"
params = {
    "id": 2017462
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "application/json",
}

try:
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()  # Проверяем ошибки

    data = response.json()
    print(response.json())
    df = pd.DataFrame(data['rows'])

    print("Статус код:", response.status_code)
    print("\nDataFrame:")
    print(df.loc[:,'cols'])
    print(df.loc[:, 'cols'][0].keys())

except requests.exceptions.RequestException as e:
    print("Ошибка при выполнении запроса:", e)
except ValueError as e:
    print("Ошибка при обработке JSON:", e)