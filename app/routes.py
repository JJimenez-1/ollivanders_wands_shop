from app import app
from main import *


@app.route('/')
def show_inventory():
    text_in_front = "----------- Inventory right now -----------<br/>"
    inventory = inventario.get_items()
    for item in inventory:
        text_in_front = text_in_front + "<br/>" + item
    return text_in_front


@app.route('/update_inventory')
def update_inventory():
    text_in_front = "----------- Inventory updated -----------<br/>"
    updated_inventory = inventario.update_quality()
    for item in updated_inventory:
        text_in_front = text_in_front + "<br/>" + item
    return text_in_front


if __name__ == "__main__":
    app.run()
