from fastapi import FastAPI
from schemas.user  import UserInfo

app=FastAPI()

@app.get('/')
async def root():
    return {"message":"Hello World"}


@app.get('/user')
def user(data:UserInfo):
    return {"data":data}
    
