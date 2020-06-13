from typing import List
from fastapi import APIRouter, HTTPException
from app.pi.models import AuthorOut, AuthorIn, AuthorUpdate
from app.pi import db_manager

authors = APIRouter()

@authors.get('/', response_model=List[AuthorOut])
async def get_authors():
    return await db.manager.get_all_authors()

@authors.post('/', response_model=AuthorOut, status_code=201)
async def create_author(payload: AuthorIn):
    author_id = await db_manager.add_author(payload)
    response = {"id": author_id, **payload.dict()}
    return response

@author.get('/{id}', response_model=AuthorOut)
async def get_author(id:int):
    author = db_manager.get_book(id)
    if not author:
        raise HTTPException(status_code=404, detail='Author not Found')
    return author

@author.put('/{id}', response_model=AuthorOut)
async def update_author(id:int):
    author = db_manager.get_book(id)
    if not author:
        raise HTTPException(status_code=404, detail='Author not Found')
    update_data = payload.dict(exclude_unset = True)
    author_id_db = AuthorIn(**author)

    update_author= author_id_db.copy(update=update_data)
    return await db_manager.update_author(id, update_author)

@authors.delete("/{id}/", response_model=None)
async def delete_book(id: int):
    author= await db_manager.get_book(id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return await db_manager.delete_author(id)


