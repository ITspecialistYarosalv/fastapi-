from sqlalchemy import (Column,Integer,MetaData,String,Table,create_engine)
from databases import Database

DATABASE_URL = "mysql://root:20041980api@localhost/project1"

engine = create_engine(DATABASE_URL)
metadata = MetaData()
Article = Table(
    "article",
    metadata,
    Column("id",Integer,primary_key = True),
    Column("title",String(100)),
    Column("description", String(100))
)
database = Database(DATABASE_URL)

User = Table(
    "user",
    metadata,
    Column("id",Integer,primary_key = True),
    Column("username",String(100)),
    Column("password", String(200))
)