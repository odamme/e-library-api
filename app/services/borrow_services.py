from schemas.borrow_record_schema import Borrow
from database.in_memory import borrow_records
from crud.users import users, user_crud
from crud.books import books, book_crud
from crud.book_borrows import borrow_crud
from services.book_services import book_service
from datetime import datetime

class BorrowService():
    
    @staticmethod
    def borrow_book(user_id:int, book_id:int):
        user = user_crud.get_user_by_id(user_id)
        book = book_crud.get_book_by_id(book_id)
        
        if not user:
            raise Exception("User not Found")
        if not user.is_active:
            raise Exception("User not Active")
        if not book:
            raise Exception("Book Not Found")
        if not book.is_available:
            raise Exception("Book Not Available")
    
        for record in borrow_records.values():
            if (
                record.user_id == user_id and
                record.book_id == book_id and
                not record.return_date
            ):
                raise Exception("Book is already borrowed")
            
        borrow_record = borrow_crud.create_borrow_record(user_id, book_id)
        
        book_service.mark_book_as_unavailable(book_id)
        
        return borrow_record
    
    @staticmethod
    def return_book(borrow_id:int):
        borrow_record = borrow_crud.get_borrow_record_by_id(borrow_id)
        book_id =  borrow_record.book_id
        if not borrow_record:
            raise Exception("Borrow record not found")
        
    
        borrow_record.return_date = datetime.now()
    
              
        book_service.mark_book_as_available(book_id)
        
        return borrow_record
    
borrow_service = BorrowService()