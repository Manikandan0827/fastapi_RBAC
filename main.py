from fastapi import FastAPI
from database import engine
from models import SQLModel
from routes import auth_routes, project_routes

app = FastAPI()

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

app.include_router(auth_routes.router)
app.include_router(project_routes.router)
