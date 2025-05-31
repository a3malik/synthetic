
def anyargs(**kwargs):
   print(kwargs)

print("Printing the kwargs functionlity")

d1={'x':1,'y':2}
'''this one does not work --> anyargs(d1)'''

'''These two given below work, notice **d1 will expand the dict to keyword arguments--> x=1, y=2'''
anyargs(**d1)
#OR
anyargs(v=-2)

'''Now try to decipher the pydantic BaseModel functionality used in FastAPI post method'''

from pydantic import BaseModel

class PrintBook():
   def __init__(self,id,title):
      print(id,title)

class BookRequest(BaseModel):
   id: int 
   title: str

def create_book(book_request: BookRequest):
   PrintBook(**book_request)

print('Printing FastAPI post method functionality')
if __name__=='__main__':
   '''Here model dump will convert the returned values to a dict'''
   print(BookRequest(**{'id':1,'title':'mynotes'}).model_dump())
   create_book(BookRequest(id=2,title='mybooks').model_dump())
