from fastapi import APIRouter, HTTPException
from app.models import Book
from app.db import books

router = APIRouter()

@router.post("/books/")
def create_book(book: Book):
    if any(b.id == book.id for b in books):
        raise HTTPException(status_code=400, detail="Book already exists")
    books.append(book)
    return book

@router.get("/books/{book_id}")
def read_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@router.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    for i, book in enumerate(books):
        if book.id == book_id:
            books[i] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

@router.delete("/books/{book_id}")
def delete_book(book_id: int):
    for i, book in enumerate(books):
        if book.id == book_id:
            del books[i]
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")

@router.patch("/books/{book_id}/unavailable")
def mark_book_unavailable(book_id: int):
    for book in books:
        if book.id == book_id:
            book.is_available = False
            return book
    raise HTTPException(status_code=404, detail="Book not found")
