from sqlalchemy import create_engine, MetaData, Table, Column, Integer

# MySQL 데이터베이스 URL
DATABASE_URL = "mysql+pymysql://root:password@db:3306/test_db"

# 데이터베이스 엔진 생성
engine = create_engine(DATABASE_URL)

# MetaData 객체 생성
metadata = MetaData()

# 테이블 정의
count_table = Table(
    "count",  # 테이블 이름
    metadata,
    Column("id", Integer, primary_key=True),  # 기본 키 컬럼
    Column("count", Integer, default=0)      # 카운터 값
)

# 데이터베이스 초기화 함수
def init_db():
    metadata.create_all(engine)
