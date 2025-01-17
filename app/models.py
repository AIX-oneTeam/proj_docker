from sqlalchemy import Column, Integer
from . import Base  

class Counter(Base):
    __tablename__ = 'counter'  
    id = Column(Integer, primary_key=True, index=True)  
    count = Column(Integer, default=0)  

    def __repr__(self):
        return f"<Counter(id={self.id}, count={self.count})>"
    

    