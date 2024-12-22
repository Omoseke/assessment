E-Library API System
Overview
The E-Library API System is a FastAPI-based project that provides an API for managing an online library. It supports managing users, books, and borrowing records with appropriate validation and business logic.

Features

User Management:

Create, read, update, and delete users.
Deactivate a user account.
Book Management:

Create, read, update, and delete books.
Mark a book as unavailable.
Borrow Operations:

Borrow a book if it’s available and the user is active.
Return a book and update its availability status.
View borrowing records for a specific user or all users.
Requirements
Python 3.8+
FastAPI
Uvicorn
Installation
1