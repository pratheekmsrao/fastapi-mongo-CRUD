import dotenv
import os
dotenv.load_dotenv()
import pymongo

import urllib.parse

username = urllib.parse.quote_plus(os.getenv("MONGO_USERNAME"))
password = urllib.parse.quote_plus(os.getenv("MONGO_PASSWORD"))

# client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@cluster0.ahcv1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# db = client.test
# print(client.list_database_names())
# db=client.get_database("UsersDB")
# print(db.list_collection_names())
# col=db.get_collection("Users")
# mydict = { "name": "John", "address": "Highway 37" }
# col.insert_one(mydict)




def get_db():
    client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@cluster0.ahcv1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.test
    db=client.get_database("UsersDB")
    # try:
    #     yield db
    # finally:
    #     db.close()
    return db
