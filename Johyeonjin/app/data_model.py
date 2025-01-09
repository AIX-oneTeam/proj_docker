from sqlalchemy import Column, Integer, MetaData, Table

metadata = MetaData()

count_table = Table(
   "count_table", #테이블 이름
   metadata, # 테이블과 연결할 메타데이터 객체
    Column("id", Integer, primary_key=True),
    Column("count", Integer) 
)