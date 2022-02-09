from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None


# GET
# POST
# PUT
# DELETE

inventory = {}


@app.get("/")
def home():
    return {"Data": "Testing"}


@app.get("/about")
def about():
    return {"Data": "About"}


@app.get("/get-item/{item_id}")
def get_item(
    item_id: int = Path(
        None, description="The ID of the item you like to view.", gt=0
    )
):
    return inventory[item_id]


@app.get("/get-by-name/{item_id}")
def get_item(*, item_id: int, name: Optional[str] = None, test: int):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    return {"Data": "Not found"}

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item ID already exists"}
    
    inventory[item_id] = item
    return inventory[item_id]