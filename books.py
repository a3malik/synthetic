
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def fast_api():
    return {'message':'Important Books!'}


BOOKS=[
{'title':'Geeta',
 'year':'5000 BC',
 'about': 'This book is the collection of sermon delivered to Arjun by Sri Krishn, in the battlefield of Kurukshetr'
},
{'title':'Mahabharat',
 'year':'5000 BC',
 'about': 'This is an epic revolving around the Kuru clan ruling in Hastinapur, the life of Kings and Queens and the battle of\
 Kurukshetr'
},
{'title':'Ramayan',
 'year':'7000 BC',
 'about': 'This is an epic about the examplary life of Ram and Sita'
},
 
]

@app.get("/books")
async def read_all_books():
    return ([x['title'] for x in BOOKS])

@app.get("/books/{path_parameter}")
async def return_selected(path_parameter):
    return ([ {x['title']:x['about']} for x in BOOKS if x.get('title')==path_parameter][0])

@app.get("/{dynamic_param}")
async def return_dynamic_dict(dynamic_param):
   return {"endpoint_text":dynamic_param}
