FROM python:3.12

WORKDIR /app

# backend 폴더의 파일들만 복사
COPY backend/ .
COPY requirements.txt .

# 의존성 설치
RUN pip install --no-cache-dir -r requirements.txt

# FastAPI 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
