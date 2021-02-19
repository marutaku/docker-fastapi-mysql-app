from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from app.utilities.session import SimpleSessions
from app.models.auth import AuthModel
app = FastAPI()
templates = Jinja2Templates(directory="templates")

session = SimpleSessions()


@app.get("/")
def index(request: Request):
    """
    トップページを返す
    :param request: Request object
    :return:
    """
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/register")
def register(request: Request):
    """
    新規登録ページ
    :param request:
    :return:
    """
    return templates.TemplateResponse("register.html", {"request": request})


@app.post("/register")
def create_user(username: str = Form(""), password: str = Form("")):
    auth_model = AuthModel()
    auth_model.create_user(username, password)


