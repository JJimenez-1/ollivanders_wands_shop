from app import app
from main import *


@app.route('/')
def show_inventory():
    string = ""
    inventary = inventario.get_items()
    for item in inventary:
        string = string + item
    return string.__repr__()


@app.route('/update_inventory')
def update_inventory():
    return inventario.update_quality()


if __name__ == "__main__":
    app.run()
