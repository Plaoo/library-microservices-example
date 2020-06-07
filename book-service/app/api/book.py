from typing import List
from fastapi import APIRouter, HTTPException
from app.api.models import BookOut,BookIn, BookUpdate
from app.api import db_manager
from app.api.service import is_book_present

books = APIRouter()

@books.post('/', response_model=BookOut, status_code=201)
async def create_book(payload:BookIn):
    for book_id in payload.book_id:
        if not is_book_present(book_id):
            raise HTTPException(status_code=404, detail=f"Book with id: {book_id} not found")
        book_id = await db_manager.add_book(payload)
        response = {
            'id':book_id,
            **payload.dict()
        }
        return response

@book.get('/', response_model=List[BookOut])
async def get_books():
    return await db_manager.get_all_books()

@book.get('/{id}', response_model=BookOut)
async def get_book(id: int):
    book = await db_manager.get_book(id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book



