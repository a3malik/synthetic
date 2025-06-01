from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Optional

app = FastAPI()

class BookRequest(BaseModel):
    id: Optional[int] = Field(default=None)
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    rating: int = Field(gt=0, le=5)
    date_published: int = Field(gt=0)

    model_config = {
        "json_schema_extra":{
            "example":{"title":"A New Book","author":"Amit","rating":1,"date_published":2025}
        }
    }

class Book():
    def __init__(self, id: int, title: str, author: str, rating: int, date_published: int = 2025):
        self.id = id
        self.title = title
        self.author = author
        self.rating = rating
        self.date_published = date_published

    def get_book(self):
        return {
            "title": self.title,
            "author": self.author,
            "date_published": self.date_published,
        }
    
BOOKS = [
    Book(1,"Godan", "Premchand",4,1926),
    Book(2,"Rajtarangini", "kalhan",5,1033),
    Book(3,"Mansarovar", "Premchand",4,1928),
    Book(4,"kamayani", "Jaishankar Prasad",4,1933),
    Book(5,"Hindi Sahitya Ka Itihas", "Acharya Ramchandra Shukl",4,1929),
    Book(6,"Raseedi Tikat", "Amrita Preetam",3,1956),
]


@app.get("/books")
async def get_all_books():
    return [ book.get_book() for book in BOOKS ]

@app.get("/books/{bookid}")
async def get_book_by_id(bookid: int):
    '''We need to use int function if we do not specify bookid to be int
      in the parameter above'''
    #return [ book.get_book() for book in BOOKS if book.id == int(bookid) ]
    return [ book.get_book() for book in BOOKS if book.id == bookid ]

@app.get("/books/")
async def get_book_by_rating(rating: int):
    return [x.get_book() for x in BOOKS if x.rating == rating]

@app.post("/create_book")
async def create_book(book_request: BookRequest):
    new_book=Book(**book_request.model_dump())
    BOOKS.append(find_book_by_id(new_book))

def find_book_by_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book

@app.put("/books/update_book")
async def update_book(book_request: BookRequest):
    for book in BOOKS:
        if book.id == book_request.id:
            book.title = book_request.title
            book.author = book_request.author
            book.rating = book_request.rating
            book.date_published = book_request.date_published
            return {"message": "Book updated successfully"}

@app.delete("/books/delete_book/")
async def delete_book(bookid: int):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == bookid:
            del BOOKS[i]
            return {"message": "Book deleted successfully"}

@app.get("/books/published/")
async def get_book_by_year(year: int):
    return [ x.get_book() for x in BOOKS if x.date_published == year ]