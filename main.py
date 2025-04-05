from gspread import Client, Spreadsheet, Worksheet, service_account
from os import getenv
from dotenv import load_dotenv
from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

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