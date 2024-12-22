from fastapi import FastAPI
from .routes import user_routes
from .routes import book_routes
from .routes import borrow_routes

app =FastAPI()

app.include_router(user_routes.router)
app.include_router(book_routes.router)
app.include_router(borrow_routes.router)

@app.get("/")
def home():
    return {"message": "Welcome!"}
