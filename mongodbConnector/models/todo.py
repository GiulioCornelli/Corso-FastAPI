from pydantic import BaseModel

# definiazione del modello Todo, che sarà uguale nel db
class Todo(BaseModel):
    name: str
    description: str
    completed: bool