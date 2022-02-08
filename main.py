from fastapi import FastAPI, Path
from typing import Optional

app = FastAPI()


# GET
# POST
# PUT
# DELETE

inventory = {1: {"name": "Milk", "price": 3.99, "brand": "Regular"}}


@app.get("/")
def home():
    return {"Data": "Testing"}


@app.get("/about")
def about():
    return {"Data": "About"}


@app.get("/get-item/{item_id}")
def get_item(
    item_id: int = Path(
        None, description="The ID of the item you like to view.", gt=0, lt=2
    )
):
    return inventory[item_id]


@app.get("/get-by-name")
def get_item(name: Optional[str] = None):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"Data": "Not found"}
