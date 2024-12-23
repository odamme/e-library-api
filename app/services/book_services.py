from schemas.book_schemas import  Book, PatchBook
from database.in_memory import books
from crud.books import books, book_crud
from fastapi import HTTPException, status

class BookService():
    
    @staticmethod
    def mark_book_as_unavailable(book_id:int):
        book = book_crud.get_book_by_id(book_id)
        if not book:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not Found")
        
        if book.is_available != True:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Book marked as unavailable")     
        book.is_available = False
            
        return
    
    @staticmethod
    def mark_book_as_available(book_id:int):
        book = book_crud.get_book_by_id(book_id)
        
        if not book:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not Found")
        
        if book.is_available == True:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Book is already available")
        book.is_available = True
        
        return
    
    @staticmethod
    def validate_book_availabity(book_id:int):
        book = book_crud.get_book_by_id(book_id)
        if not book:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not Found")
       
        if book.is_available == True:
            return True
        return False
        
book_service = BookService()