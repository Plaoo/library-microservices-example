from app.api.models import AuthorIn, AuthorOut, AuthorUpdate
from app.api.db import authors, database

async def add_author(payload: AuthorIn):
    query = authors.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get_all_authors():
    query = authors.select()
    return await database.fetch_all(query=query)

async def get_author(id: int):
    query = authors.select(authors.c.id==id)
    return await database.fetch_one(query=query)

async def delete_author(id: int):
    query = authors.delete().where(authors.c.id == id)
    return await database.execute(query=query)

async def update_author(id: int, payload: AuthorIn):
    query = authors.update().where(authors.c.id == id).values(**payload.dict())
    return await database.execute(query=query)
