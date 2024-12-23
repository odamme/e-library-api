API Endpoints
-------------------
**- User Endpoints**

```plaintext
POST   /v1/users/          Create new user
GET    /v1/users/          Retrieve all users
GET    /v1/users/{id}      Retrieve a specific user
PUT    /v1/users/{id}      Update user details
PATCH  /v1/users/{id}      Deactivate user
DELETE /v1/users/{id}      Delete user
```
**- Book Endpoints**

```plaintext
POST   /v1/books/          Add new book
GET    /v1/books/          List books
GET    /v1/books/{id}      Retrieve specific book
PUT    /v1/books/{id}      Update book details
PATCH  /v1/books/{id}      Mark book unavailable
DELETE /v1/books/{id}      Remove book
```
**- Borrow Endpoints**

```plaintext
POST   /v1/borrows/        Record book borrow
GET    /v1/borrows/        List all borrowing records
GET    /v1/borrows/{id}    Get user's borrowing history
PATCH  /v1/borrows/{id}    Return book
```

**Application setup**

1. **Environment Configuration**
   ```bash
   # Clone repository
   git clone <repository-url>
   cd e-library-api

   # Create a virtual environment
   python -m venv venv
   source venv/bin/activate  # macOS
   \venv\Scripts\activate.bat   # Windows

   # Install dependencies
   pip install -r requirements.txt
