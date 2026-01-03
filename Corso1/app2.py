from fastapi import FastAPI, HTTPException
from src.schemas import PostCreate, PostResponse


app = FastAPI()




text_posts = {
    1: {"title": "First Post", "content": "This is my first post!"},
    2: {"title": "Second Post", "content": "This is my second post!"},
    3: {"title": "Introduction to FastAPI", "content": "Building high-performance APIs with Python."},
    4: {"title": "The Power of uv", "content": "Revolutionizing Python package management with Rust."},
    5: {"title": "Clean Architecture", "content": "Separating concerns for maintainable software."},
    6: {"title": "Dockerizing Python", "content": "How to containerize your applications efficiently."},
    7: {"title": "Async/Await Patterns", "content": "Mastering concurrency in modern Python code."},
    8: {"title": "Unit Testing with Pytest", "content": "Ensuring code quality through automated tests."},
    9: {"title": "SQLAlchemy 2.0", "content": "The new way of interacting with databases in Python."},
    10: {"title": "Deployment Strategies", "content": "CI/CD pipelines for seamless production releases."}
}

@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit: # se esiste un limite lo imposta per i valori di ritorno
        return list(text_posts.values())[:limit]
    else:
        return text_posts


@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_posts:
        return HTTPException(status_code=404, detail="Post not found")
    else:
        return text_posts.get(id)
    

@app.post("/posts")
def create_post(post: PostCreate) -> PostResponse: # definiamo il tipo di ritorno della funzione con -> PostResponse
    new_post = {"title": post.title, "content": post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post

@app.delete("/posts/{id}")
def delete_post(id: int):
    if id not in text_posts:
        return HTTPException(status_code=404, detail="Post not found")
    else:
        text_posts.pop(id)
        return {"detail": "Post deleted", "post": id}