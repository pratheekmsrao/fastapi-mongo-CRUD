from fastapi import Body, Depends, FastAPI
from db import get_db

from schemas.user import UpdateAddress, UserAddress, UserInfoIn, UserLogin

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
    # TODO add incrementing userid
    db=get_db("UsersDB")
    col=db.get_collection("Users")
    id=col.insert_one(user.dict())
    return {"message":"success","inser_id":str(id.inserted_id)}




@app.post('/login')
async def login(data:UserLogin=Body(...)):
    db=get_db("UsersDB")
    col=db.get_collection("Users")
    user=col.find_one({'email':data.email,'password':data.password})
    if user:
        return {"message":f'User {data.email} found',"status":200}
    else:
        return {"message":f'user{data.email} not found','status':404}

# @app.post('/user')
# async def create_user(data:UserInfoIn):
#     user.update(data)
#     return {"data":user}

@app.post('/address')
async def create_address(address:UserAddress=Body(...)):
    # TODO integrate user with UserAddress
    # by using UserInfoIn
    db=get_db("UsersDB")
    col=db.get_collection("Address")
    id=col.insert_one(address.dict())
    return {"message":"success","inser_id":str(id.inserted_id)}

@app.get('/address')
async def get_address(user:str):
    # TODO integrate user with UserAddress
    # by using UserInfoIn
    # TODO make return address using pydantic model
    db=get_db("UsersDB")
    col=db.get_collection("Address")
    address=col.find_one({'username':user})
    if address:
        return {"message":f'address for  {user} found',"status":200}
    else:
        return {"message":f'address for {user} not found','status':404}
    
@app.post('/update_address')
async def update_address(address:UserAddress=Body(...)):
    # TODO integrate user with UserAddress
    # by using UserInfoIn
    db=get_db("UsersDB")
    col=db.get_collection("Address")
    u_address={k:v for k,v in address.dict().items() if v is not None}
    res=col.update_one({'username':address.username},{'$set':address.dict()})
    if res.modified_count==1:
        return {"message":f'address for  {address.username} updated',"status":200}
    else:
        return {"message":f'address for {address.username} not found','status':404}