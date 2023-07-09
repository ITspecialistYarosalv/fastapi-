from fastapi import APIRouter,HTTPException,status
from .Schemas import UserSchema,UserSchemaIn
from .db import  User,database
from typing import List
from  passlib.hash import pbkdf2_sha256
rounter = APIRouter(tags = ['Users'])

@rounter.post('/users/',status_code= status.HTTP_201_CREATED,response_model =UserSchemaIn )
async def insert_articles(article:UserSchema):
    hash_password = pbkdf2_sha256.hash(article.password)
    query = User.insert().values(username= article.username,password =hash_password)
    last_recorde_id = await  database.execute(query)
    return {**article.dict(),"id":last_recorde_id}

@rounter.get('/users/',response_model=List[UserSchemaIn])
async  def get_articles():
    query = User.select()
    return await database.fetch_all(query)

@rounter.get('/users/{id}',response_model=UserSchemaIn)
async def get_details(id:int):
    query = User.select().where(id == User.c.id)
    myarticle = await database.fetch_one(query)

    if not myarticle:
        return HTTPException
    return {**myarticle}

@rounter.put('/users/{id}',status_code=status.HTTP_202_ACCEPTED)
async def put_article(id:int,article:UserSchema):
    query = User.update().where(User.c.id == id).values(username = article.username, password = article.password)
    await database.execute(query)
    return {"message":"It's all done"}

@rounter.delete('/users/{id}/',status_code=status.HTTP_204_NO_CONTENT)
async def del_article(id:int):
    query = User.delete().where(User.c.id == id)
    await  database.execute(query)
    return {"message": "It's all done"}
