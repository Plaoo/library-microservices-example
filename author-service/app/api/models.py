from pydantic import BaseModel
from typing import List, Optional

class AuthorIn(BaseModel):
    firstname: str
    surname: str
    year_of_birth: int
    year_of_death: Optional[int] = None
    nationality: str

class AuthorOut(AuthorIn):
    id: int

class AuthorUpdate(AuthorIn):
    firstname: Optional[str] = None
    surname: Optional[str] = None
    year_of_birth: Optional[int] = None
    year_of_death: Optional[int] = None
    nationality: Optional[str] = None

