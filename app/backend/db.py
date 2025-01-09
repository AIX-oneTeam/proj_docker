import sqlite3

DATABASE_NAME = 'db.sqlite3'

# 데이터베이스 연결 및 테이블 생성
def create_db():
    conn = sqlite3.connect(DATABASE_NAME)  # 데이터베이스 파일 생성
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS number (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            value INTEGER
        )
    ''')
    cursor.execute('INSERT INTO number (value) VALUES (0)')  # 초기값 0으로 삽입
    conn.commit()
    conn.close()

# 숫자 값 가져오기
def get_number():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT value FROM number WHERE id = 1")
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else 0

def update_number(new_value):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE number SET value = ? WHERE id = 1", (new_value,))
    conn.commit()
    conn.close()

# 숫자 +1
def increment_number():
    current_value = get_number()
    new_value = current_value + 1
    update_number(new_value)
    return new_value

# 숫자 -1
def decrement_number():
    current_value = get_number()
    new_value = current_value - 1
    update_number(new_value)
    return new_value
