from fastapi import FastAPI,Depends,status,HTTPException
from .db import metadata,database,engine,Article
from . import articles,users,auth
metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()

@app.get('/')
async def Index():
    return {'message':"Hello world"}

@app.on_event("shutdown")
async def startup():
    await database.disconnect()

app.include_router(articles.rounter)
app.include_router(users.rounter)
app.include_router(auth.rounter)