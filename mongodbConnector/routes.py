from fastapi import APIRouter
from models.todo import Todo
from config.database import collection_name
from schemas.schema import list_serial
from typing import List
from fastapi import HTTPException
from bson import ObjectId

router = APIRouter()

# GET request Method

@router.get("/todos")
async def get_todos():
    todos = list_serial(collection_name.find())

    return todos

# Post request Method

@router.post("/add_todo")
async def add_todo(todo: Todo):
    try:
        collection_name.insert_one(dict(todo))
        return {"message": "Todo added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# @router.post("/add_mutiple_todos")
# async def add_multiple_todos(todos: List[Todo]):
#     try:
#         docs = [dict(t) for t in todos]
#         collection_name.insert_many(docs)
#         return {"message": "Multiple todos added successfully"}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
    

# Put request Method
@router.put("/update_tudo/{id}")
async def update_todo(id: str, todo: Todo):
    collection_name.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": dict(todo)}
    )
    return {"message": "Todo updated successfully"}



