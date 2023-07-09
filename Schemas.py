from pydantic import BaseModel
from typing import Optional
class ArticleSchema(BaseModel):
    title:str
    description:str

class ArticleSchemaIn(ArticleSchema):
    id:int

class UserSchema(BaseModel):
    username:str
    password:str

class UserSchemaIn(UserSchema):
    id:int

class LoginSchema(BaseModel):
    username:str
    password:str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None