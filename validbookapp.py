from fastapi import FastAPI
from pydantic import BaseModel,Field

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
    title: str = Field(min_length=2)
    author: str = Field(min_length=2)
    description: str = Field(min_length=3,max_length=100)
    rating: float = Field(gt=0, le=5)

class SmallRequest(BaseModel):
    id: int
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    #rating: float = Field(gt=0, le=5)

class SmallBook():
    def __init__(self, id: int, title: str, author: str):
        self.id = id
        self.title = title
        self.author = author

    def get_book(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author
        }
    
BOOKS = [
    Book(1, "Godan", "Munshi Premchand", "A novel by Munshi Premchand", 4.5),
    Book(2, "kamayani", "Jaishankar Prasad", "Poetry by Jaishankar Prasad", 4.0),
    Book(3, "Hindi Sahitya Ka Itihas", "Acharya Ramchandra Shukl", "History of Hindi Literature", 4.0),
    Book(4, "Rajtarangini", "kalhan", "History of Indian Royal families", 4.0),
    Book(5, "Mansarovar", "Munshi Premchand", "Collection of stories", 4.0),
]

SMALLBOOKS = [
    SmallBook(1,"Godan", "Premchand"),
    SmallBook(2,"Rajtarangini", "kalhan"),
    SmallBook(3,"Mansarovar", "Premchand"),
]

'''
{"id":6, 
 "title":"Raseedi Tikat", 
 "author":"Amrita Preetam", 
 "description":"Autobiograpdy", 
 "rating":4.0
}
'''


@app.get("/books")
async def get_all_books():
    return [ book.get_book() for book in SMALLBOOKS ]
    #return [ book.get_book() for book in BOOKS ]

@app.post("/create_book")
async def create_book(book_request: SmallRequest):
    new_book=SmallBook(**book_request.model_dump())
    #new_book=Book(**book_request.model_dump())
    SMALLBOOKS.append(find_book_id(new_book))

def find_book_id(book: SmallBook):
    if len(SMALLBOOKS)>0:
        book.id = SMALLBOOKS[-1].id + 1
        #book.id = BOOKS[-1].id + 1
    else:
        book.id = 1
    return book