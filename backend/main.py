from fastapi import FastAPI
from sqlalchemy import select, update
from database import engine, count_table, init_db
from fastapi.middleware.cors import CORSMiddleware

# 데이터베이스 초기화
init_db()

# FastAPI 애플리케이션 초기화
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 카운터 값 가져오기
@app.get("/count")
def read_count():
    with engine.connect() as conn:
        query = select(count_table).where(count_table.c.id == 1)
        result = conn.execute(query).fetchone()
        if not result:
            conn.execute(count_table.insert().values(id=1, count=0))
            conn.commit()
            return {"count": 0}
        return {"count": result[1]}  # count 컬럼의 인덱스 사용

# 카운터 값 증가
@app.post("/increment")
def increase_count():
    with engine.connect() as conn:
        query = select(count_table).where(count_table.c.id == 1)
        result = conn.execute(query).fetchone()
        if result:
            new_value = result[1] + 1  # count 컬럼의 인덱스 사용
            conn.execute(update(count_table).where(count_table.c.id == 1).values(count=new_value))
            conn.commit()
            return {"count": new_value}
        return {"error": "Counter not found"}

# 카운터 값 감소
@app.post("/decrement")
def decrease_count():
    with engine.connect() as conn:
        query = select(count_table).where(count_table.c.id == 1)
        result = conn.execute(query).fetchone()
        if result:
            new_value = result[1] - 1  # count 컬럼의 인덱스 사용
            conn.execute(update(count_table).where(count_table.c.id == 1).values(count=new_value))
            conn.commit()
            return {"count": new_value}
        return {"error": "Counter not found"}
