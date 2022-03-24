
from typing import Optional
from pydantic import BaseModel

class UserLogin(BaseModel):
    email : str
    password : str

class UserInfo(BaseModel):
    first_name:str
    middle_name:Optional[str]=None
    last_name:str
    age:Optional[int]=None
    email:str

class UserAddress(BaseModel):
    address_line1:str
    address_line2:Optional[str]=None
    city:str
    state:str
    country:str
    zip_code:str


