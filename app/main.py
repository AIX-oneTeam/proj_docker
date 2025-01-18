from fastapi import FastAPI, Depends, Request, Form
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from . import db, services

app = FastAPI()

# Jinja2 템플릿 경로 설정
templates = Jinja2Templates(directory="app/templates")

@app.on_event("startup")
def startup():
    db.create_tables()

# 의존성 주입을 통해 데이터베이스 세션을 가져오는 함수
def get_db():
    session = db.SessionLocal()
    try:
        yield session
    finally:
        session.close()

@app.get("/")
def read_counter(request: Request, db: Session = Depends(get_db)):
    counter = services.get_counter(db)
    return templates.TemplateResponse("index.html", {"request": request, "number": counter.count if counter else 0})

@app.post("/update")
def update_counter(cal: str = Form(...), db: Session = Depends(get_db)):
    # 카운터 값 업데이트
    if cal == "increment":
        services.increment_counter(db)
    elif cal == "decrement":
        services.decrement_counter(db)
    
    # 카운터 값 반환
    counter = services.get_counter(db)
    return {"message": "Counter updated", "number": counter.count if counter else 0}