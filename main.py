# from fastapi import FastAPI
# from api import api_router

# app = FastAPI()

# app.include_router(api_router)
from fastapi import FastAPI
from api import api_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
def home():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()
    
app.include_router(api_router)