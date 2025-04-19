from gspread import Client
from sheet_class import Sheet
from os import getenv
from dotenv import load_dotenv
from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

table_link ='https://docs.google.com/spreadsheets/d/'
table_id = "1VKkXzFKOL85l8AiTdgk7fqBVAlsFUYw71vQS09ZOYTg"

Client = Sheet.client_init_json()
print(Client, 'Клиент')
print(table_link + table_id, 'Таблица')

load_dotenv()

TOKEN = getenv("TOKEN")

app = FastAPI()


@app.get("/")
def read_root():
    """Test method"""
    html_content = "<h2>Sheet.Master!</h2>"
    table = Sheet.get_table_by_key(Client, table_id)
    Sheet.create_row(table, 'fd', [1,2, 2])
    return HTMLResponse(content=html_content)

@app.post('/create')
async def create_table(name:str = Body(embed=True, min_length=3, max_length=20)):
    """create table from google sheet"""
    return name

@app.get("/health")
def read_root():
    """Test method"""
    html_content = "<h2>good!</h2>"
    return HTMLResponse(content=html_content)

