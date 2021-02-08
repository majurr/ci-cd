import platform
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    plataforma = platform.system()
    versao = platform.version()
    uname = platform.uname()
    
    return {
        "plataforma" : plataforma,
        #"versão" : versao,
        #"uname" : uname
    }
