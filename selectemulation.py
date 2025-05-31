from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import os


def get_all_data_versions(url, save_dir=r'C:\Users\HYPER\PycharmProjects\Classes 4 wave\saturday\DataExample\Data\htmls'):
    """
    Получает все версии данных, эмулируя взаимодействие с элементами data-item

    :param url: URL целевой страницы
    :param save_dir: Директория для сохранения версий
    """
    # Настройка браузера
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')

    driver = webdriver.Chrome(options=options)
    actions = ActionChains(driver)

    try:
        # Создаем папку для сохранения
        os.makedirs(save_dir, exist_ok=True)

        # Открываем страницу
        print(f"Открываем страницу: {url}")
        driver.get(url)

        # Ожидаем загрузки элементов данных
        wait = WebDriverWait(driver, 15)
        data_items = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'dl.data-item')))

        if not data_items:
            print("Элементы данных не найдены!")
            return

        print(f"Найдено {len(data_items)} элементов данных")

        # Сохраняем исходную версию
        save_data_version(driver, save_dir, "initial")

        # Обрабатываем каждый элемент данных
        for idx, item in enumerate(data_items, 1):
            try:
                print(f"\nОбработка элемента {idx}/{len(data_items)}")

                # Прокручиваем к элементу
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", item)
                time.sleep(1)

                # Эмулируем наведение мыши
                actions.move_to_element(item).pause(1).perform()
                time.sleep(1)

                # Кликаем (если нужно)
                item.click()
                time.sleep(2)  # Ждем загрузки данных

                # Сохраняем текущее состояние
                save_data_version(driver, save_dir, f"version_{idx}")

                # Дополнительно: получаем data-id если есть
                data_id = item.get_attribute('data-id')
                if data_id:
                    print(f"Data ID: {data_id}")

            except Exception as e:
                print(f"Ошибка при обработке элемента {idx}: {e}")

    finally:
        driver.quit()


def save_data_version(driver, save_dir, version_name):
    """Сохраняет текущую версию страницы"""
    filename = f"{version_name}.html"
    filepath = os.path.join(save_dir, filename)

    # Получаем текущий HTML
    html = driver.page_source

    # Сохраняем
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Сохранена версия: {filename}")


# URL для обработки
target_url = "https://data.admhmao.ru/opendata/8602020249-tseny_na_gsm_g_surgut"

# Запускаем сбор версий
get_all_data_versions(target_url)