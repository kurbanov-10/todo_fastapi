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
    return "<h1>Blog App ishlayapti 🚀</h1>"

app.include_router(api_router)