import os
import requests


def download_file(url, save_dir=r'C:\Users\HYPER\PycharmProjects\Classes 4 wave\saturday\DataExample\Data\downloads'):
    """
    Скачивает файл по URL и сохраняет в указанную директорию

    :param url: URL файла для скачивания
    :param save_dir: Директория для сохранения (по умолчанию 'downloads')
    :return: Путь к сохраненному файлу
    """
    try:
        # Создаем директорию, если ее нет
        os.makedirs(save_dir, exist_ok=True)

        # Получаем имя файла из URL
        filename = os.path.basename(url.split('=')[-1])

        # Полный путь для сохранения
        filepath = os.path.join(save_dir, filename)

        # Заголовки для имитации браузера
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        # Скачиваем файл
        print(f"Скачивание файла {filename}...")
        response = requests.get(url, headers=headers, stream=True)
        response.raise_for_status()  # Проверяем на ошибки

        # Сохраняем файл
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        print(f"Файл успешно сохранен: {filepath}")
        return filepath

    except Exception as e:
        print(f"Ошибка при скачивании файла: {e}")
        return None


# URL для скачивания
file_url = "https://data.admhmao.ru/bitrix/redirect.php?event1=file&event2=opendata&event3=/opendata/csv/2017462/data/data-20250415T104832-structure-20250415T104813.csv&goto=/opendata/csv/2017462/data/data-20250415T104832-structure-20250415T104813.csv"

# Вызываем функцию скачивания
download_file(file_url)