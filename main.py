import os
from dotenv import load_dotenv
from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

load_dotenv()

TOKEN = os.getenv("TOKEN")

print(TOKEN)
 
app = FastAPI()
 
@app.get("/")
def read_root():
    html_content = "<h2>Sheet.Master!</h2>"
    return HTMLResponse(content=html_content)
@app.post('/create')
async def create_table(name:str = Body(embed=True, min_length=3, max_length=20)):
    return name
