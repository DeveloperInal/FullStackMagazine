from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from contextlib import asynccontextmanager
from core.database.model import create_tables
from loguru import logger
from api.v1.get_method import router as get_router
from api.v1.set_method import router as set_router
from api.v1.delete_method import router as delete_router
from prometheus_fastapi_instrumentator import Instrumentator

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables() # создание таблицы при запуске сервера
    logger.info("Starting FastAPI server")
    try:
        yield
    finally:
        logger.info("Stopping FastAPI server")

app = FastAPI(lifespan=lifespan)
app.include_router(get_router)
app.include_router(set_router)
app.include_router(delete_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

Instrumentator().instrument(app).expose(app)

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True) # для деплоя на Heroku
