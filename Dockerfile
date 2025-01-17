FROM python:3.11.2

# 2. 작업 디렉토리를 설정합니다.
WORKDIR /dockerProj01 

# 3. 의존성 파일을 복사하고 설치합니다.
COPY requirements.txt .

# 4. 필요한 Python 패키지들을 설치합니다.
RUN pip install --no-cache-dir -r requirements.txt  

# 5. 애플리케이션 소스를 복사합니다.
COPY . .  

# 6. FastAPI 앱을 실행하는 명령어를 설정합니다.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]