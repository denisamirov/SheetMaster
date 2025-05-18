from gspread import Client
from sheet_class import Sheet
from os import getenv
from dotenv import load_dotenv
from fastapi import FastAPI, Path, Body, HTTPException
from fastapi.responses import HTMLResponse
import logging
from logger import logger_setup

logger_setup()

client = Sheet.client_init_json()

load_dotenv()

TOKEN = getenv("TOKEN")
table_link = getenv("TABLE_LINK")
TABLE_ID = getenv("TABLE_ID")

app = FastAPI()

@app.get("/")
def read_root():
    """Test method"""
    html_content = "<h2>Sheet.Master</h2>"
    return HTMLResponse(content=html_content)

@app.post('/create/{object}')
async def create_table(
    object:str = Path(min_length=3, max_length=20), 
    name_sheet:str = Body(embed=True, min_length=1, max_length=20),
    rows:list = Body(embed=True)
    ):
    
    if object not in ["rows", "sheet_list"]:
        raise HTTPException(status_code=400, detail="Invalid object type")
    
    table = Sheet.get_table_by_key(client, TABLE_ID)
    
    if object == 'rows':
        Sheet.create_row(table, name_sheet , rows)
    if object == 'sheet_list':
        Sheet.create_sheet(table, name_sheet)
        
    return 

@app.get("/health")
def read_root():
    """Test method"""
    html_content = "<h2>Good!</h2>"
    return HTMLResponse(content=html_content)
