from fastapi import APIRouter, HTTPException
from app.models import BorrowRecord
from app.db import borrow_records, users, books
from datetime import date

router = APIRouter()

@router.post("/borrow/")
def borrow_book(record: BorrowRecord):
    user = next((u for u in users if u.id == record.user_id and u.is_active), None)
    book = next((b for b in books if b.id == record.book_id and b.is_available), None)
    
    if not user:
        raise HTTPException(status_code=400, detail="User is not active or does not exist")
    if not book:
        raise HTTPException(status_code=400, detail="Book is unavailable or does not exist")
    if any(r.book_id == record.book_id for r in borrow_records if r.return_date is None):
        raise HTTPException(status_code=400, detail="Book already borrowed by this user")

    record.borrow_date = date.today()
    books[books.index(book)].is_available = False
    borrow_records.append(record)
    return record

@router.patch("/borrow/{record_id}/return")
def return_book(record_id: int):
    for record in borrow_records:
        if record.id == record_id:
            if record.return_date is not None:
                raise HTTPException(status_code=400, detail="Book already returned")
            record.return_date = date.today()
            book = next(b for b in books if b.id == record.book_id)
            book.is_available = True
            return record
    raise HTTPException(status_code=404, detail="Borrow record not found")

@router.get("/borrow/user/{user_id}")
def get_borrow_records_by_user(user_id: int):
    user_records = [r for r in borrow_records if r.user_id == user_id]
    if not user_records:
        raise HTTPException(status_code=404, detail="No borrow records found for this user")
    return user_records

@router.get("/borrow/")
def get_all_borrow_records():
    return borrow_records
