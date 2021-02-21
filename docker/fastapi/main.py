import utils
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"msg": "hello"}

@app.get("/tables/")
def show_tables():
    db = utils.DB()
    tables = db.select("show tables;")
    return {"tables": tables}
