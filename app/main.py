from fastapi import FastAPI
from app.routes import user, book, borrow

app = FastAPI()

app.include_router(user.router, prefix="/user", tags=["User"])
app.include_router(book.router, prefix="/book", tags=["Book"])
app.include_router(borrow.router, prefix="/borrow", tags=["Borrow"])
