from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import mysql.connector

app = FastAPI()

# CORS 설정 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 도메인 허용 (특정 도메인만 허용하려면 변경)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 데이터베이스 연결 함수
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="db",  # Docker Compose에서 정의한 MySQL 서비스 이름
            user="root",
            password="root",
            database="counter_db"
        )
        return connection
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {e}")

# Pydantic 모델 정의
class CounterUpdate(BaseModel):
    action: str

# Counter 값을 가져오는 엔드포인트
@app.get("/counter")
def get_counter():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT value FROM counter WHERE id = 1")
    result = cursor.fetchone()
    connection.close()
    if not result:
        raise HTTPException(status_code=404, detail="Counter not found")
    return {"value": result["value"]}

# Counter 값을 업데이트하는 엔드포인트
@app.post("/counter")
def update_counter(update: CounterUpdate):
    connection = get_db_connection()
    cursor = connection.cursor()
    if update.action == "increment":
        cursor.execute("UPDATE counter SET value = value + 1 WHERE id = 1")
    elif update.action == "decrement":
        cursor.execute("UPDATE counter SET value = value - 1 WHERE id = 1")
    else:
        raise HTTPException(status_code=400, detail="Invalid action")
    connection.commit()
    connection.close()
    return {"message": "Counter updated"}

# 루트 엔드포인트 추가 (테스트용)
@app.get("/")
def read_root():
    return {"message": "Welcome to the Counter API"}
