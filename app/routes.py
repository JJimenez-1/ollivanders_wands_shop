from app import app
from main import *


@app.route('/')
def show_inventory():
    front_end = "----------- Inventory right now -----------<br/>"
    actual_inventory = inventory.get_items()
    for item in actual_inventory:
        front_end = front_end + "<br/>" + item
    return front_end


@app.route('/update_inventory')
def update_inventory():
    front_end = "----------- Inventory updated -----------<br/>"
    updated_inventory = inventory.update_quality()
    for item in updated_inventory:
        front_end = front_end + "<br/>" + item
    return front_end


if __name__ == "__main__":
    app.run()
