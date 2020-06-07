from app.api.models import BookIn, BookOut, BookUpdate
from app.api.db import book, database
import logging

log = logging.getLogger(__name__)


async def add_book(payload: BookIn):
    query = book.insert().values(**payload.dict)
    return await database.execute(query=query)


async def get_all_books():
    query = book.select()
    return await database.fetch_all(query=query)


async def get_book(id):
    query = book.select(book.c.id == id)
    return await database.fetch_one(query=query)


async def delete_book(id: int):
    query = book.delete().where(book.c.id == id)
    return await database.execute(query=query)


async def update_movie(id: int, payload: BookIn):
    query = book.update().where(book.c.id == id).values(**payload.dict())
    return await database.execute(query=query)
