from sqlalchemy import Column, Integer, MetaData, Table


metadata = MetaData()

count = Table(
   "count",
   metadata,
    Column("id", Integer, primary_key=True),
    Column("count", Integer) 
)