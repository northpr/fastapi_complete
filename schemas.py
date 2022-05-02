from pydantic import BaseModel

# Come from the user
class UserBase(BaseModel): # Type of data that we receive from the user
    username: str
    email: str
    password: str

class UserDisplay(BaseModel): # To display only username and password
    username: str
    email: str
    class Config():
        orm_mode = True # Allow the system to return database data to our format automatically