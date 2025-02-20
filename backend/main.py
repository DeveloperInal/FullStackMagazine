from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from contextlib import asynccontextmanager
from loguru import logger
from api.v1.admin import router as admin_router
from api.v1.card import router as card_router
from api.v1.promocode import router as promocode_router
from api.v1.tgbot import router as tgbot_router
from prometheus_fastapi_instrumentator import Instrumentator

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting FastAPI server")
    try:
        yield
    finally:
        logger.info("Stopping FastAPI server")

app = FastAPI(lifespan=lifespan)
app.include_router(promocode_router)
app.include_router(card_router)
app.include_router(admin_router)
app.include_router(tgbot_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

Instrumentator().instrument(app).expose(app)

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
