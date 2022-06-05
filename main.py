from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from routers.deals import router as deals_router


app = FastAPI()

app.include_router(deals_router)


@app.get("/")
def main_page():
    return HTMLResponse(content=open("./frontend/index.html").read())
