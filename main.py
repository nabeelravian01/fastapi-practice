from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"data": {"name": "Nabeel"}}


@app.get("/about")
def about():
    return {"data": "about page"}
