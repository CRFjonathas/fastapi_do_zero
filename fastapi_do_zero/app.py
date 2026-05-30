from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {"Mensagem": "Olá, Mundo!"}