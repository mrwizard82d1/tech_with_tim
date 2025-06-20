from typing import Optional

from fastapi import FastAPI

app = FastAPI()


inventory = {
    1: {
        "name": "Milk",
        "price": 3.99,
        "brand": "HillFarm",
    }
}


# This is a silly example but illustrates multiple path components
@app.get("/get-item/{item_id}/{brand}")
def get_item_with_brand(item_id: int, brand: Optional[str] ):
    if brand:
        return inventory[item_id][brand]
    else:
        return inventory[item_id]
