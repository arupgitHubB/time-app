from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def dashboard():
    with open("dashboard.html", "r") as f:
        return f.read()
