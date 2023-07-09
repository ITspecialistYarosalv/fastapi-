from fastapi import APIRouter,HTTPException,status,Depends
from  fastapi.security import OAuth2PasswordRequestForm
from .Schemas import LoginSchema
from .db import  User,database
from .Token import create_access_token
from passlib.hash import pbkdf2_sha256
from typing import List
rounter = APIRouter(tags=['Login'])

@rounter.post('/login/')
async def login(request:OAuth2PasswordRequestForm = Depends()):
    query = User.select().where(request.username == User.c.username)
    log = await database.fetch_one(query)

    if not log:
        raise HTTPException(status_code=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    if  not pbkdf2_sha256.verify(request.password,log.password) :
        raise HTTPException(status_code=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

    access_token = create_access_token(
        data={"sub": log.username}
    )
    return {"access_token": access_token, "token_type": "bearer"}
