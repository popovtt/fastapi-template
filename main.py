import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_bravo():
    return {"msg": "Hello BravoShop"}


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)