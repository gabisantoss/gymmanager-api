from fastapi import FastAPI
from .routes.alunos import router as members_router

app = FastAPI()

@app.get("/")
async def root():
    return {"health": "ok"}

app.include_router(members_router)
