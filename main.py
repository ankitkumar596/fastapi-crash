from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Tea(BaseModel):
    id: int
    name: str
    type: str
    origin: str

teas: List[Tea] = []

@app.get("/")
def read_root():
    return {"Message": "Welcome to the chai aur code house!"}

@app.get("/teas")
def read_teas():
    return teas

@app.post("/teas")
def create_tea(tea: Tea):
    teas.append(tea)
    return tea

@app.put("/teas/{tea_id}")
def update_tea(tea_id: int, updated_tea: Tea):
    for index, existing_tea in enumerate(teas):
        if existing_tea.id == tea_id:
            teas[index] = updated_tea
            return updated_tea
    return {"Error": "Tea not found"}

@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):
    for index, existing_tea in enumerate(teas):
        if existing_tea.id == tea_id:
            deleted_tea = teas.pop(index)
            return deleted_tea
    return {"Error": "Tea not found"}



