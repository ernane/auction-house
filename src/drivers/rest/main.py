from fastapi import FastAPI

from src.drivers.rest.exception_handlers import exception_container
from src.drivers.rest.routers import auction

app = FastAPI()

app.include_router(auction.router)

exception_container(app)
