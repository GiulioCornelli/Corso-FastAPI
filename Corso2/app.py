from fastapi import FastAPI

app = FastAPI()


all_todos = [
    {
        "todo_id": 1,
        "todo_name": "Configurare Ambiente",
        "todo_description": "Installare uv e sincronizzare le dipendenze del progetto."
    },
    {
        "todo_id": 2,
        "todo_name": "Definire Modelli Database",
        "todo_description": "Creare le classi SQLAlchemy per i Todo e i Post."
    },
    {
        "todo_id": 3,
        "todo_name": "Sviluppare Endpoint POST",
        "todo_description": "Implementare la logica per aggiungere nuovi task alla lista."
    },
    {
        "todo_id": 4,
        "todo_name": "Validazione Pydantic",
        "todo_description": "Creare gli schemi per validare l'input dell'utente."
    },
    {
        "todo_id": 5,
        "todo_name": "Gestione Errori",
        "todo_description": "Aggiungere HTTPException per gestire ID non trovati."
    },
    {
        "todo_id": 6,
        "todo_name": "Integrazione Database",
        "todo_description": "Sostituire la lista in memoria con una tabella SQLite reale."
    },
    {
        "todo_id": 7,
        "todo_name": "Sviluppo Frontend",
        "todo_description": "Creare una semplice interfaccia per visualizzare i todo."
    },
    {
        "todo_id": 8,
        "todo_name": "Test di Integrazione",
        "todo_description": "Verificare che il database e l'API comunichino correttamente."
    },
    {
        "todo_id": 9,
        "todo_name": "Documentazione Swagger",
        "todo_description": "Aggiungere descrizioni ai parametri per la doc automatica."
    },
    {
        "todo_id": 10,
        "todo_name": "Deploy Finale",
        "todo_description": "Configurare il server per rendere l'app accessibile online."
    }
]


@app.get("/helloword")
def get_helloword():
    return {"message": "Hello World"}


@app.get("/todos/{todo_id}")
def get_todo_byid(todo_id: int):
    for todo in all_todos:
        if todo["todo_id"] == todo_id:
            return todo
    return {"message": "Todo not found"}

@app.get("/todos")
def get_todos(first_n : int = None): #specifichiamo un parametro opzionale che inseriremo nell' url host/todos?first_n=3
    if first_n is not None:
        return all_todos[:first_n] # se il parametro è specificato, ritorniamo solo i primi n todo
    else:
        return all_todos
    


@app.post("/todos")
def create_todo(todo: dict):
    new_todo_id = max(todo["todo_id"] for todo in all_todos) + 1

    new_todo = {
        "todo_id": new_todo_id,
        "todo_name": todo["todo_name"],
        "todo_description": todo["todo_description"]
    }

    all_todos.append(new_todo)
    return {"message": "add a new todo","content": new_todo}