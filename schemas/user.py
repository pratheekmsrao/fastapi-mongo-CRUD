
from typing import Optional
from pydantic import BaseModel





class UserLogin(BaseModel):
    email : str
    password : str

class UserAddress(BaseModel):
    username:str
    address_line1:str
    address_line2:Optional[str]=None
    city:str
    state:str
    country:str
    zip_code:str

class UpdateAddress(BaseModel):
    username:Optional[str]=None
    address_line1:Optional[str]=None
    address_line2:Optional[str]=None
    city:Optional[str]=None
    state:Optional[str]=None
    country:Optional[str]=None
    zip_code:Optional[str]=None

class UserInfoIn(BaseModel):
    first_name:str
    middle_name:Optional[str]=None
    last_name:str
    age:Optional[int]=None
    email:str
    address:UserAddress





# class UserCreate(BaseModel):
#     info:UserInfoIn
#     address:UserAddress




