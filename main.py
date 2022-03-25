from fastapi import Body, Depends, FastAPI
from db import get_db

from schemas.user import UserAddress, UserInfoIn, UserLogin

import dotenv
import os
dotenv.load_dotenv()


app=FastAPI()

userlogin={
    'email':'email@abc.com',
    'password':'passwrodabc'
}

userinfo={
        'first_name':'firstname1',
    'middle_name':'midlename1',
    'last_name':'lastname1',
    'age':20,
    'email':'abc@abc.com',
}

useraddress={
    'abc@abc.com':{
        'address_line1':'add1',
    'address_line2':'add2',
    'city':'city1',
    'state':'state1',
    'country':'count1',
    'zip_code':'zip1',}
}

user={
    'user':''
}



@app.get('/')
async def root():
    return {"message":"Hello World"}

@app.post('/register')
async def register(user:UserLogin=Body(...)):
    db=get_db()
    col=db.get_collection("Users")
    id=col.insert_one(user.dict())
    return {"message":"success","inser_id":str(id.inserted_id)}




@app.post('/login')
async def login(data:UserLogin):
    userlogin.update(data)
    print('before userlogin',userlogin)
    print('userlogin',userlogin,userlogin.get(data.email))
    return {"data":userlogin}

@app.post('/user')
async def create_user(data:UserInfoIn):
    user.update(data)
    return {"data":user}

@app.post('/address')
async def address(address:UserAddress):
    useraddress.update(address)
    return {"data":useraddress}
    
