from gspread import service_account, Client, Spreadsheet

class Sheet:
    """Класс для работы с библиотекой gspread"""
    @staticmethod
    def create_row(table: Spreadsheet, sheet_name: str, data: list):
        """Создание записи"""
        worksheet = table.worksheet(sheet_name)
        worksheet.append_row(data)

    @staticmethod
    def info_about_sheets():
        """Информация о таблице"""
        return

    @staticmethod
    def get_table_by_key(client: Client, table_key: str):
        """получить таблицу c помощью ключа"""
        return client.open_by_key(table_key)

    @staticmethod
    def client_init_json():
        """Создание клиента для работы с Google Sheets."""
        return service_account(filename='creds.json')

    @staticmethod
    def get_table_by_id(client: Client, table_url: str):
        """Получение таблицы из Google Sheets по ID таблицы."""
        return client.open_by_key(table_url)

    # @staticmethod
    # def test_get_table(table_url: str, table_key: str):
    #     """Тестирование получения таблицы из Google Sheets."""
    #     client = self.client_init_json()
    #     table = self.get_table_by_url(client, table_url)
    #     print('Инфо по таблице по ссылке: ', table)
    #     table = self.get_table_by_id(client, table_key)
    #     print('Инфо по таблице по id: ', table)

    @staticmethod
    def create_worksheet(table: Spreadsheet, title: str, rows: int, cols: int):
        """Create a new worksheet"""
        return table.add_worksheet(title, rows, cols)
