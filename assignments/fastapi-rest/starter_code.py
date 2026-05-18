from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Optional

app = FastAPI(title="FastAPI - REST API Assignment")

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float

# In-memory storage for example purposes
items: Dict[int, Item] = {}

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI assignment API"}

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    item = items.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/items/", response_model=Item, status_code=201)
def create_item(item: Item):
    if item.id in items:
        raise HTTPException(status_code=400, detail="Item with this id already exists")
    items[item.id] = item
    return item
