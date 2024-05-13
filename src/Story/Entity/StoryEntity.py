from sqlite3 import Date
from pydantic import BaseModel

class Story(BaseModel): 
    id: int
    name:	str
    text:	str
    date:	Date