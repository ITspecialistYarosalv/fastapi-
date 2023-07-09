from fastapi import APIRouter,HTTPException,status,Depends
from .Schemas import ArticleSchema,ArticleSchemaIn,UserSchema
from .db import  Article,database
from typing import List
from .Token import get_current_user

rounter = APIRouter(tags=['Articles'])

@rounter.post('/articles/',status_code= status.HTTP_201_CREATED,response_model =ArticleSchemaIn )
async def insert_articles(article:ArticleSchema):
    query = Article.insert().values(title= article.title,description = article.description)
    last_recorde_id = await  database.execute(query)
    return {**article.dict(),"id":last_recorde_id}

@rounter.get('/articles/',response_model=List[ArticleSchemaIn])
async  def get_articles(current_user:UserSchema = Depends(get_current_user)):
    query = Article.select()
    return await database.fetch_all(query)

@rounter.get('/articles/{id}',response_model=ArticleSchemaIn)
async def get_details(id:int):
    query = Article.select().where(id == Article.c.id)
    myarticle = await database.fetch_one(query)

    if not myarticle:
        return HTTPException
    return {**myarticle}

@rounter.put('/articles/{id}',status_code=status.HTTP_202_ACCEPTED)
async def put_article(id:int,article:ArticleSchema):
    query = Article.update().where(Article.c.id == id).values(title = article.title, description = article.description)
    await database.execute(query)
    return {"message":"It's all done"}

@rounter.delete('/articles/{id}/',status_code=status.HTTP_204_NO_CONTENT)
async def del_article(id:int):
    query = Article.delete().where(Article.c.id == id)
    await  database.execute(query)
    return {"message": "It's all done"}