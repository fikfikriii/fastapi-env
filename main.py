from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

class Items(BaseModel):
    nama: str

data_mahasiswa = {
    18220000: {
        "Nama": "Test"
    }
}

app = FastAPI()

@app.get("/mahasiswa/{nim}")
def get_mahasiswa(nim: int):
    if nim in data_mahasiswa:
        return data_mahasiswa[nim]
    else:
        return {"Data mahasiswa tidak ditemukan"}

@app.post("/mahasiswa")
def post_mahasiswa(nim: int, item: Items):
    if nim in data_mahasiswa:
        return {"Error: Data mahasiswa sudah terdaftar"}

    data_mahasiswa[nim] = {"nama": item.nama}
    return data_mahasiswa[nim]
