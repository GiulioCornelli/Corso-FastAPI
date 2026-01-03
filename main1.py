import uvicorn


if __name__ == "__main__":
    uvicorn.run( # permette di avviare il server uvicorn con diverse caratteristiche
        "Corso1.app:app", # nome cartella.nome_file:nome_istanza_app
        host="0.0.0.0",
        port=8000,
        reload=True # ogni volta modifichiamo il codice, il server si riavvia automaticamente
    )