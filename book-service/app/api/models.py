from pydantic import BaseModel
from typing import List, Optional

class BookIn(BaseModel):
    title: str
    year: int
    genres: List[str]
    authors_id: List[str]

class BookOut(BookIn):
    id: int

class BookUpdate(BookIn):
    title: Optional[str] = None
    year: Optional[int] = None
    genres: Optional[List[str]] = None
    authors_id: Optional[List[str]] = None

