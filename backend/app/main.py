from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.api.router import api_router
from app.db.bootstrap import bootstrap_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    bootstrap_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(api_router)
