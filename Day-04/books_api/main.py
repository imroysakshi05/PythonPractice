from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

books = {}
next_id = 1


class BookCreate(BaseModel):
    title: str
    author: str


class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None


class BookResponse(BaseModel):
    id: int
    title: str
    author: str

@app.get("/")
def root():
    return {"message": "Books API is running"}

@app.get("/books")
def get_books():
    return list(books.values())


@app.get(
    "/books/{book_id}",
    response_model=BookResponse
)
def get_book(book_id: int):

    if book_id not in books:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return books[book_id]


@app.post(
    "/books",
    response_model=BookResponse,
    status_code=status.HTTP_201_CREATED
)
def create_book(book: BookCreate):

    global next_id

    new_book = {
        "id": next_id,
        "title": book.title,
        "author": book.author
    }

    books[next_id] = new_book
    next_id += 1

    return new_book


@app.patch(
    "/books/{book_id}",
    response_model=BookResponse,
    response_model_exclude_unset=True
)
def update_book(
    book_id: int,
    updates: BookUpdate
):

    if book_id not in books:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    update_data = updates.model_dump(
        exclude_unset=True
    )

    books[book_id].update(update_data)

    return books[book_id]


@app.delete(
    "/books/{book_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_book(book_id: int):

    if book_id not in books:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    del books[book_id]