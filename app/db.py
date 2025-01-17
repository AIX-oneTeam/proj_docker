from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

user = os.environ.get("MYSQL_USER")
password = os.environ.get("MYSQL_PASSWORD")
host = os.environ.get("MYSQL_HOST")
port = os.environ.get("MYSQL_PORT", 3307)
name = os.environ.get("MYSQL_DATABASE")

# DB 연결 URL
DB_URL = f'mysql+pymysql://{user}:{password}@{host}:{port}/{name}'

# SQLAlchemy 엔진 생성
engine = create_engine(DB_URL, echo=True)

# SQLAlchemy Base 생성
Base = declarative_base()

# SessionLocal 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 테이블을 생성하는 함수
def create_tables():
    Base.metadata.create_all(bind=engine)