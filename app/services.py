from sqlalchemy.orm import Session
from .models import Counter

def get_counter(db: Session):
    return db.query(Counter).first()  

def increment_counter(db: Session):
    counter = db.query(Counter).first()
    if counter:
        counter.count += 1
    else:
        counter = Counter(count=1)
        db.add(counter)
    db.commit()

def decrement_counter(db: Session):
    counter = db.query(Counter).first()
    if counter:
        counter.count -= 1
    else:
        counter = Counter(count=-1)
        db.add(counter)
    db.commit()
