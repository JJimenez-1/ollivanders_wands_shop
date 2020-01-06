from app import app
from main import *


@app.route('/')
def show_inventory():
    inventary = inventario.get_items()
    return inventary.__repr__()


@app.route('/update_inventory')
def update_inventory():
    return inventario.update_quality()


if __name__ == "__main__":
    app.run()
