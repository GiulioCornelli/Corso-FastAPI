from pydantic import BaseModel

# allinterno di questa classe definiamo le schema dei vari dati che utilizzeremo nella nostra applicazione

class PostCreate(BaseModel):
    title: str
    content: str
    
class PostResponse(PostCreate):
    title: str
    content: str