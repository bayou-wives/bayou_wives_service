from fastapi import FastAPI

from app.api.api_router import api_router

app = FastAPI(
    title='Bayou Wives Service'
)

app.include_router(api_router)
