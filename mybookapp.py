from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

class Book:

    id: int
    title: str
    author: str
    description: str
    rating: float

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

    def get_book(self):
        return {
            "title": self.title,
            "author": self.author,
        }
    
class BookRequest(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: float
    
BOOKS = [
    Book(1, "Godan", "Munshi Premchand", "A novel by Munshi Premchand", 4.5),
    Book(2, "kamayani", "Jaishankar Prasad", "Poetry by Jaishankar Prasad", 4.0),
    Book(3, "Hindi Sahitya Ka Itihas", "Acharya Ramchandra Shukl", "History of Hindi Literature", 4.0),
    Book(4, "Rajtarangini", "kalhan", "History of Indian Royal families", 4.0),
    Book(5, "Mansarovar", "Munshi Premchand", "Collection of stories", 4.0),
]
#{"id":6, "title":"Raseedi Tikat", "author":"Amrita Preetam", "description":"Autobiograpdy", "rating":4.0}

@app.get("/books")
async def get_all_books():
    #return [ book.title for book in BOOKS ]
    return BOOKS

@app.post("/create_book")
async def create_book(book_request: BookRequest):
    #BOOKS.append(book_request)
    new_book=Book(**book_request.model_dump())
    BOOKS.append(new_book)