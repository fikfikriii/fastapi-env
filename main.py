from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"NIM": "18220097",
            "Nama": "Muhamad Fikri Nurohman"
            }
