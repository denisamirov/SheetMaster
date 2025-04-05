from gspread import service_account

class Sheet:
    def create():
        pass

    def info_about_sheets():
        pass

    def get_table_but_key():
        pass

    def client_init_json():
        """Создание клиента для работы с Google Sheets."""
        return service_account(filename='creds.json')

# def get_table_by_id(client: Client, table_url):
#     """Получение таблицы из Google Sheets по ID таблицы."""
#     return client.open_by_key(table_url)
# def test_get_table(table_url: str, table_key: str):
#     """Тестирование получения таблицы из Google Sheets."""
#     client = client_init_json()
#     table = get_table_by_url(client, table_url)
#     print('Инфо по таблице по ссылке: ', table)
#     table = get_table_by_id(client, table_key)
#     print('Инфо по таблице по id: ', table)


# if __name__ == '__main__':
#     test_get_table(table_link, table_id)
#     def create_worksheet(table: Spreadsheet, title: str, rows: int, cols: int):
#         return table.add_worksheet(title, rows, cols)

# def test_create_worksheet():
#     client = client_init_json()
#     table = get_table_by_id(client, table_id)
#     rez = create_worksheet(table, 'НовыйРабочийЛист', rows=15, cols=10)
#     print(rez)