from app import app
from main import *


@app.route('/')
def show_inventory():
    front_end = "----------- Inventory right now -----------<br/>"
    inventory.get_items()
    for item in items_accepted:
        front_end = front_end + "<br/>" + item.__repr__()
    return front_end


@app.route('/update_inventory')
def update_inventory():
    front_end = "----------- Inventory updated -----------<br/>"
    inventory.update_quality()
    for item in items_accepted:
        front_end = front_end + "<br/>" + item.__repr__()
    return front_end


@app.route('/update_inventory/<days>')
def update_inventory_days(days):
    front_end = "----------- Update at Day " + days + " -----------<br/>"
    for day in range(1, int(days) + 1):
        inventory.update_quality()
    for item in items_accepted:
        front_end = front_end + "<br/>" + item.__repr__()
    return front_end


if __name__ == "__main__":
    app.run()
