
from fastapi import FastAPI, Body

app = FastAPI()

@app.get("/")
async def home():
    return {'message':'Important Books!'}


BOOKS=[
{'title':'Geeta',
 'year':'5000 BC',
 'about': 'This book is the collection of sermon delivered to Arjun by Sri Krishn, in the battlefield of Kurukshetr',
 'author': 'Ved Vyas',
},
{'title':'Mahabharat',
 'year':'5000 BC',
 'about': 'This is an epic revolving around the Kuru clan ruling in Hastinapur, the life of Kings and Queens and the battle of\
 Kurukshetr',
 'author': 'Ved Vyas',

},
{'title':'Ramayan',
 'year':'7000 BC',
 'about': 'This is an epic about the examplary life of Ram and Sita',
 'author': 'Valmiki',
},
{'title':'deleteme',
 'year':'2023',
 'about':'this is just junk data to be deleted',
 'author':'Amit',
}
 
]

@app.get("/books")
async def read_all_books():
    return ([{x['title']:x['author']} for x in BOOKS])

@app.get("/books/{path_parameter}")
async def return_selected(path_parameter):
    '''Pass a title of the book as path_parameter'''
    return ([ {x['title']:x['about']} for x in BOOKS if x.get('title')==path_parameter][0])

@app.get("/{dynamic_param}")
async def return_dynamic_dict(dynamic_param):
   '''Same as path_parameter, but working just like an echo'''
   return {"endpoint_text":dynamic_param}

@app.get("/books/")
async def return_with_query(param):
    '''Make use of a query like q?param=value'''
    l1=[ x['title'] for x in BOOKS if x['author'].casefold()==param.casefold()]
    return l1

@app.post("/books/create_book")
async def create_book(new_book=Body()):
    '''Template for a post request, no database connection yet'''
    BOOKS.append(new_book)

@app.put("/books/update_books")
async def update_books(updated_book=Body()):
    '''Remove spaces from the author name for a book title passed in body of put method.
    Also take a closer look at this function, we are comparing a title in the if condition,
    does it look like a state comparison? Would this end point be still restful?'''
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i]['author'] = BOOKS[i]['author'].replace(' ','')

'''Can we use put and post interchangably?  they both have a body that can be used 
in functions processing the request provided by end point'''

@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            del BOOKS[i]
            break