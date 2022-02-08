from fastapi import FastAPI, Path

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
    item_id: int = Path(None, description="The ID of the item you like to view")
):
    return inventory[item_id]
