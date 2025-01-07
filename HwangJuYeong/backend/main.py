# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
from mysql.connector import Error

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost"],  # 프론트엔드가 실행되는 도메인만 허용
    allow_credentials=True,
    allow_methods=["*"],  # 필요한 HTTP 메서드만 허용
    allow_headers=["*"],  # 모든 헤더를 허용
)

# MySQL 연결 함수
def get_db_connection():
    return mysql.connector.connect(
        host="db",
        user="count",
        password="count",
        database="counter_db"
    )

@app.get("/count")
def get_count():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT value FROM counter WHERE id = 1")
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return {"count": result[0] if result else 0}

@app.post("/increment")
def increment():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE counter SET value = value + 1 WHERE id = 1")
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "incremented"}

@app.post("/decrement")
def decrement():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE counter SET value = value - 1 WHERE id = 1")
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "decremented"}