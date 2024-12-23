from pydantic import BaseModel, EmailStr
from typing import Optional

class BookBase(BaseModel):
    title: str
    author:str

class BookStatus(BaseModel):
    is_available:bool = True

class CreateBook(BookBase):
    title: str = "The genesis of the Earth"
    author:str = "John Doe"

class Book(BookBase, BookStatus):
    id: int = 100001
    
class PatchBook(BaseModel):
    title: Optional[str] = "Geospatial Analysis"
    author:Optional[str] = "Damilola Oladeji"