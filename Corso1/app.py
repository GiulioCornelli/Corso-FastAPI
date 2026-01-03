# import per fastapi
from fastapi import FastAPI, HTTPException, File, UploadFile, Form, Depends
from src.schemas import PostCreate, PostResponse

# import per il database
from src.db import Post, get_async_session, create_db_and_tables, engine
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from sqlalchemy import select

@asynccontextmanager
async def lifespan(app:FastAPI):
    await create_db_and_tables()
    yield
    await engine.dispose()



# creazione istanza fastapi
app = FastAPI(lifespan=lifespan)


# endpoint per creare un post
@app.post("/upload")
async def uploand_file(file: UploadFile = File(...),caption: str = Form(""),session: AsyncSession = Depends(get_async_session)):
    post = Post(
        caption=caption,
        url="dummyurl",
        file_type="photo",
        file_name="dummy name"
    )
    session.add(post)
    await session.commit()
    await session.refresh(post)
    return post

@app.get("/feed")
async def get_feed(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(Post).order_by(Post.created_at.desc()))
    posts = [row[0] for row in result.all()]
    
    posts_data = []
    for post in posts:
        posts_data.append(
            {
                "id": str(post.id),
                "caption": post.caption,
                "url": post.url,
                "file_type": post.file_type,
                "file_name": post.file_name,
                "created_at": post.created_at.isoformat()
            }
        )
    return {"posts":posts_data}