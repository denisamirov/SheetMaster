from gspread import Client, Spreadsheet, Worksheet, service_account
from os import getenv
from dotenv import load_dotenv
from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

def client_init_json() -> Client:
    """Создание клиента для работы с Google Sheets."""
    return service_account(filename='creds.json')

table_link ='https://docs.google.com/spreadsheets/d/'
table_id = "1VKkXzFKOL85l8AiTdgk7fqBVAlsFUYw71vQS09ZOYTg"

def get_table_by_key(client, table_key):
    """Получение таблицы из Google Sheets по id."""
    return client.open_by_key(table_key)


Client = client_init_json()
print(Client, 'Клиент')
print(table_link + table_id, 'Таблица')

load_dotenv()

TOKEN = getenv("TOKEN")

print(TOKEN)
 
app = FastAPI()
 
@app.get("/")
def read_root():
    html_content = "<h2>Sheet.Master!</h2>"
    table = get_table_by_key(Client, table_id)
    print(table, 'Таблица')
    return HTMLResponse(content=html_content)
@app.post('/create')
async def create_table(name:str = Body(embed=True, min_length=3, max_length=20)):
    return name


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