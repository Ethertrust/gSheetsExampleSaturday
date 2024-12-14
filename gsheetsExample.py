from gspread import Client, Spreadsheet, Worksheet, service_account

def client_init_json() -> Client:
    """
    Создание клиента для работы с Google Sheets.
    """
    return service_account(filename='sa\\example3-443310-d58285942731.json')



def get_table_by_id(client: Client, table_id):
    """Получение таблицы из Google Sheets по ID таблицы."""
    return

def test_get_table(client: Client, table_key: str) -> Spreadsheet:
    """Тестирование получения таблицы из Google Sheets."""
    table = client.open_by_key(table_key)
    # print('Инфо по таблице по id: ', table)
    return table

def get_worksheet_info(table: Spreadsheet) -> dict:
    """Возвращает количество листов в таблице и их названия."""
    worksheets = table.worksheets()
    worksheet_info = {
        "count": len(worksheets),
        "names": [worksheet.title for worksheet in worksheets]
    }
    return worksheet_info

def gSheetsRead(table: Spreadsheet, sheet_name: str, start_row = 2) -> list[dict]:
    """
    Извлекает данные из указанного листа таблицы Google Sheets и возвращает список словарей.

    :param table: Объект таблицы Google Sheets (Spreadsheet).
    :param sheet_name: Название листа в таблице.
    :return: Список словарей, представляющих данные из таблицы.
    """
    worksheet = table.worksheet(sheet_name)
    headers = worksheet.row_values(start_row)  # Первая строка считается заголовками

    data = []
    rows = worksheet.get_all_values()[start_row:]  # Начинаем считывать с второй строки

    for row in rows:
        row_dict = {headers[i]: value for i, value in enumerate(row)}
        data.append(row_dict)

    return data

def gSheetsUpdate(table: Spreadsheet, title: str, data: list[dict], start_row: int = 2) -> None:
    """
    Добавляет данные на рабочий лист в Google Sheets.

    :param table: Объект таблицы (Spreadsheet).
    :param title: Название рабочего листа.
    :param data: Список словарей с данными.
    :param start_row: Номер строки, с которой начнется добавление данных.
    """

    worksheet = table.worksheet(title)

    headers = data[0].keys()
    end_row = start_row + len(data) - 1
    end_col = chr(ord('A') + len(headers) - 1)

    cell_range = f'A{start_row}:{end_col}{end_row}'
    cell_list = worksheet.range(cell_range)

    flat_data = []
    for row in data:
        for header in headers:
            flat_data.append(row[header])

    for i, cell in enumerate(cell_list):
        cell.value = flat_data[i]

    worksheet.update_cells(cell_list, value_input_option = 'user_entered')

client = client_init_json()
table_id ='1-EOZVonyvq4JEh_-d0kuiUecqsPwRvTPTwd2qb_C5yU'
# table_link = 'https://docs.google.com/spreadsheets/d/1-EOZVonyvq4JEh_-d0kuiUecqsPwRvTPTwd2qb_C5yU/edit?gid=1869783570#gid=1869783570'
table = test_get_table(client, table_id)

if __name__ == '__main__':
    for key, val in get_worksheet_info(table).items():
        print(key+':', val)
    for row in gSheetsRead(table, 'Performance'):
        print(row)



