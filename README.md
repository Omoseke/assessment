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
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/e-library-api.git
cd e-library-api
Set up a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy code
pip install fastapi uvicorn
Running the Application
Start the server:

bash
Copy code
uvicorn app.main:app --reload
Access the API documentation:

Interactive Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
File Structure
bash
Copy code
e_library_api/
├── app/
│   ├── main.py        # Application entry point
│   ├── models.py      # Pydantic models
│   ├── routes/        # API routes
│   │   ├── user.py    # User-related routes
│   │   ├── book.py    # Book-related routes
│   │   └── borrow.py  # Borrow-related routes
│   ├── db.py          # In-memory database
│   └── utils.py       # Utility functions (if needed)
└── README.md          # Project instructions
API Endpoints
User Endpoints
Create a user: POST /user/
Read a user: GET /user/{user_id}
Update a user: PUT /user/{user_id}
Delete a user: DELETE /user/{user_id}
Deactivate a user: PATCH /user/{user_id}/deactivate
Book Endpoints
Create a book: POST /book/
Read a book: GET /book/{book_id}
Update a book: PUT /book/{book_id}
Delete a book: DELETE /book/{book_id}
Mark a book as unavailable: PATCH /book/{book_id}/unavailable
Borrow Endpoints
Borrow a book: POST /borrow/
Return a book: PATCH /borrow/{record_id}/return
View records for a user: GET /borrow/user/{user_id}
View all records: GET /borrow/
Testing
To run test cases, install pytest and create test files in the project. Example:

bash
Copy code
pip install pytest
pytest
Contributing
Feel free to fork the repository and submit pull requests to improve the system.
