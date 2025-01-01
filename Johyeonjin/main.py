# python에서 비동기 DB 처리를 위한 모듈
import databases
from fastapi import FastAPI, Request, Form
# HTMLResponse는 템플릿에서 렌더링된 HTML을 반환할 때 사용.
# RedirectResponse는 리다이렉션을 할 때 사용.
from fastapi.responses import HTMLResponse, RedirectResponse
# Jinja2 템플릿 엔진 사용을 위한 클래스
from fastapi.templating import Jinja2Templates
# python ORM인 sqlalchemy를 이용해 엔티티 작성
from sqlalchemy import MetaData

app = FastAPI()

# MySQL 데이터베이스 URL
# mysql+pymysql://유저이름:비밀번호@호스트주소/데이터베이스이름
DATABASE_URL = "mysql+asyncmy://root:0000@localhost/test"


# Jinja2 템플릿 디렉터리 설정
templates = Jinja2Templates(directory="templates")
# 데이터베이스 객체 생성
database = databases.Database(DATABASE_URL)
# 엔티티 설정
metadata = MetaData()

# 모델(상태)
data = {"count": 0}

# 초기 화면 렌더링
# 두번째 인자는 반환할 응답 타입 지정임.
@app.get("/", response_class=HTMLResponse)
# request 인자는 FastAPI에서 자동으로 주입해줌.
# fastapi는 request객체를 직접 사용해야함.
async def read_root(request: Request):
    # TemplatesReponse는 ModelAndView와 같은 역할을 함.
    # 다만 TemplatesResponse의 Resolver가 어떤 구조로 되어있는지는 확인 필요. 
    # 전달시 반드시 request객체를 첫 인자로 포함시켜야 함. (이는 서블릿과 유사한듯.)
    return templates.TemplateResponse("index.html", {"request": request,
                                                     "count": data["count"]})

@app.post("/update", response_class=HTMLResponse)
async def update_count(action : str = Form(...)):
    if(action == "increase"):
        data["count"] += 1
    elif(action == "decrease"):
        data["count"] -= 1
    
    return RedirectResponse(url = "/", status_code=303)


