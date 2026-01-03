import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "Corso2.app:app",
        host="0.0.0.0",
        port=8080,
        reload=True
        )