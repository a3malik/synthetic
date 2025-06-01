from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Optional

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
    id: Optional[int] = Field(default=None)
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    rating: int = Field(gt=0, le=5)

    model_config = {
        "json_schema_extra":{
            "example":{"title":"A New Book","author":"Amit","rating":1}
        }
    }

class SmallBook():
    def __init__(self, id: int, title: str, author: str, rating: int):
        self.id = id
        self.title = title
        self.author = author
        self.rating = rating

    def get_book(self):
        return {
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
    SmallBook(1,"Godan", "Premchand",4),
    SmallBook(2,"Rajtarangini", "kalhan",5),
    SmallBook(3,"Mansarovar", "Premchand",4),
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

@app.get("/books/{bookid}")
async def get_book_by_id(bookid: int):
    '''We need to use int function if we do not specify bookid to be int
      in the parameter above'''
    #return [ book.get_book() for book in SMALLBOOKS if book.id == int(bookid) ]
    return [ book.get_book() for book in SMALLBOOKS if book.id == bookid ]

@app.get("/books/")
async def get_book_by_rating(rating: int):
    return [x.get_book() for x in SMALLBOOKS if x.rating == rating]

@app.post("/create_book")
async def create_book(book_request: SmallRequest):
    new_book=SmallBook(**book_request.model_dump())
    #new_book=Book(**book_request.model_dump())
    SMALLBOOKS.append(find_book_by_id(new_book))

def find_book_by_id(book: SmallBook):
    book.id = 1 if len(SMALLBOOKS) == 0 else SMALLBOOKS[-1].id + 1
    return book

@app.put("/books/update_book")
async def update_book(book_request: SmallRequest):
    for book in SMALLBOOKS:
        if book.id == book_request.id:
            book.title = book_request.title
            book.author = book_request.author
            book.rating = book_request.rating
            return {"message": "Book updated successfully"}

#The code below does not work because book_request is a SmallRequest object,
#and it does not have get_book() method. So we end up appending SmallRequest
#to SmallBook in the SMALLBOOKS list. Then subsequent requests on SMALLBOOKS
#start throwing errors. After we have executed the PUT method once.
    '''for i in range(len(SMALLBOOKS)):
        if SMALLBOOKS[i].id == book_request.id:
            SMALLBOOKS[i] = book_request'''

@app.delete("/books/delete_book/")
async def delete_book(bookid: int):
    for i in range(len(SMALLBOOKS)):
        if SMALLBOOKS[i].id == bookid:
            del SMALLBOOKS[i]
            return {"message": "Book deleted successfully"}