from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import init_db
from auth import router as auth_router, User
from routes.api import router as api_router

app = FastAPI(title="API_REST_de_gestión_de_tareas_")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    init_db()

@app.get("/")
def root():
    return {"status": "ok", "project": "API_REST_de_gestión_de_tareas_", "auth": "/auth/login, /auth/register, /auth/me"}

app.include_router(auth_router)
app.include_router(api_router, prefix='/api')