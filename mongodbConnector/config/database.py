from pymongo import MongoClient

uri = "mongodb://mongo-root:pippo123@localhost:27017/"
client = MongoClient(uri)

db = client.todo_db

collection_name = db["todo_collection"]
