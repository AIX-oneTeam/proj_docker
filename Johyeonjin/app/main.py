# python에서 비동기 DB 처리를 위한 모듈
from contextlib import asynccontextmanager
from databases import Database
from fastapi import Depends, FastAPI, Request, Form
# HTMLResponse는 템플릿에서 렌더링된 HTML을 반환할 때 사용.
# RedirectResponse는 리다이렉션을 할 때 사용.
from fastapi.responses import HTMLResponse, RedirectResponse
# Jinja2 템플릿 엔진 사용을 위한 클래스
from fastapi.templating import Jinja2Templates
# python ORM인 sqlalchemy를 이용해 엔티티 작성

# MySQL 데이터베이스 URL
# mysql+asyncmy://유저이름:비밀번호@호스트주소/데이터베이스이름
DATABASE_URL = "mysql+asyncmy://fastapi:fastapi@db:3306/test"
database = Database(DATABASE_URL)

# FastAPI 애플리케이션 수명 주기 관리
@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await database.connect()  # 데이터베이스 연결
        await database.execute("USE test;") 
        print("Connecting to database")
    except Exception as e:
        print("Error during initialization", e)
    yield
    await database.disconnect()  # 연결 해제

app = FastAPI(lifespan=lifespan)

# Jinja2 템플릿 디렉터리 설정
templates = Jinja2Templates(directory="templates")

# 초기 화면 렌더링
# 두번째 인자는 반환할 응답 타입 지정임.
@app.get("/", response_class=HTMLResponse)
# request 인자는 FastAPI에서 자동으로 주입해줌.
# fastapi는 request객체를 직접 사용해야함.
async def read_root(request: Request):
    query = "SELECT * FROM count_table WHERE id = 1"
    if not database.is_connected:
        await database.connect()
    result = await database.fetch_one(query) 

    # TemplatesReponse는 ModelAndView와 같은 역할을 함.
    # 다만 TemplatesResponse의 Resolver가 어떤 구조로 되어있는지는 확인 필요. 
    # 전달시 반드시 request객체를 첫 인자로 포함시켜야 함. (이는 서블릿과 유사한듯.)
    return templates.TemplateResponse("index.html", {"request": request, "count": result["count"]})



@app.post("/update", response_class=HTMLResponse)
async def update_count(action : str = Form(...)):
    if not database.is_connected:
        await database.connect()
    if(action == "increase"):
        query = "UPDATE count_table SET count = count + 1 WHERE id = 1"
        await database.execute(query)   
    elif(action == "decrease"):
        query = "UPDATE count_table SET count = count - 1 WHERE id = 1"
        await database.execute(query)

    return RedirectResponse(url = "/", status_code=303)


