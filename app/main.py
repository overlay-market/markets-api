from fastapi import FastAPI

from .chain.connection import init_chain, close_chain
from .chain.contract import CONTRACTS
from .db.connection import init_db, close_db
from .db.session import client
from .routers import login, user


app = FastAPI()


@app.on_event("startup")
async def startup_event():
    init_chain(CONTRACTS)
    init_db(client)


@app.on_event("shutdown")
async def shutdown_event():
    close_chain(CONTRACTS)
    close_db(client)


app.include_router(login.router, tags=["login"])
app.include_router(user.router, prefix="/api/users", tags=["user"])
