from fastapi import FastAPI

import routes.user_routes
import routes.book_routes
import routes.borrow_routes

app =FastAPI()

app.include_router(routes.user_routes.router, prefix="/v1/users",tags=["Users"],)
app.include_router(routes.book_routes.router, prefix="/v1/books", tags=["Books"])
app.include_router(routes.borrow_routes.router, prefix="/v1/borrows", tags=["Borrow"])

@app.get("/")
def home():
    return {"message": "Welcome!"}
