from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from app.backend.db import create_db, get_number, update_number, increment_number, decrement_number

app = FastAPI()

# 템플릿 연결
templates = Jinja2Templates(directory="app/")

# 디비 생성
create_db()

# 초기 값 불러오기
@app.get("/", response_class=HTMLResponse)
async def read_number(request: Request):
    number = get_number()
    return templates.TemplateResponse("index.html", {"request": request, "number": number})

# 버튼 클릭 시 반응 함수
@app.post("/update", response_class=HTMLResponse)
async def update_number(request: Request, cal: str = Form(...)):  # Form에서 'cal' 값을 받도록 수정
    if cal == "increment":
        number = increment_number()
    elif cal == "decrement":
        number = decrement_number()
    return templates.TemplateResponse("index.html", {"request": request, "number": number})
