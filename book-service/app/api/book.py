from typing import List
from fastapi import APIRouter, HTTPException
from app.api.models import BookOut, BookIn, BookUpdate
from app.api import db_manager
from app.api.service import is_author_present
books = APIRouter()

@books.get("/", response_model=List[BookOut])
async def get_books():
    return await db_manager.get_all_books()

@books.post("/", response_model=BookOut, status_code=201)
async def create_book(payload: BookIn):
    for author_id in payload.authors_id:
        if not is_author_present(author_id):
            raise HTTPException(
                status_code=404, detail=f"Author with id: {author_id} not found"
            )
    book_id = await db_manager.add_book(payload)
    response = {"id": book_id, **payload.dict()}
    return response


@books.get("/{id}", response_model=BookOut)
async def get_book(id: int):
    book = await db_manager.get_book(id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@books.put("/{id}", response_model=BookOut)
async def update_book(id: int, payload: BookUpdate):
    book = await db_manager.get_book(id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    update_data = payload.dict(exclude_unset=True)
    if update_data.get('authors_id', False):
        for author_id in payload.authors_id:
            if not is_author_present(author_id):
                raise HTTPException(status_code=404, detail=f"Author ID not found")
    book_in_db = BookIn(**book)

    update_book = book_in_db.copy(update=update_data)
    return await db_manager.update_book(id, update_book)


@books.delete("/{id}", response_model=None)
async def delete_book(id: int):
    book = await db_manager.get_book(id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return await db_manager.delete_book(id)
