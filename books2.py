from fastapi import FastAPI, Body

app = FastAPI()

class Book:
    def __init__(self, id, title, author, decsription, rating):
        self.id = id
        self.title = title
        self.author = author
        self.decsription = decsription
        self.rating = rating

    def get_book(self):
        return {
            "title": self.title,
            "author": self.author,
        }
    
BOOKS = [
    Book(1, "Godan", "Munshi Premchand", "A novel by Munshi Premchand", 4.5),
    Book(2, "kamayani", "Jaishankar Prasad", "Poetry by Jaishankar Prasad", 4.0),
    Book(3, "Hindi Sahitya Ka Itihas", "Acharya Ramchandra Shukl", "History of Hindi Literature", 4.0),
    Book(4, "Rajtarangini", "kalhan", "History of Indian Royal families", 4.0),
    Book(5, "Mansarovar", "Munshi Premchand", "Collection of stories", 4.0),
]

@app.get("/books")
async def get_all_books():
    return [ x.get_book() for x in BOOKS]