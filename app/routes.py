from app import app
from main import *


inventory = Gildedrose([Normalitem("+5 Dexterity Vest", 10, 20), Agedbrie("Aged Brie", 2, 0), Normalitem("Elixir of the Mongoose", 5, 7), Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80), Sulfuras("Sulfuras, Hand of Ragnaros", -1, 80), Backstagepass("Backstage passes to a TAFKAL80ETC concert", 15, 20), Backstagepass("Backstage passes to a TAFKAL80ETC concert", 10, 49), Backstagepass("Backstage passes to a TAFKAL80ETC concert", 5, 49), Conjured("Conjured Mana Cake", 3, 6)])


@app.route('/')
def show_inventory():
    inventory.add_item()
    actual_inventory = inventory.get_items()
    front_end = "----------- Inventory right now -----------<br/>"
    for item in actual_inventory:
        front_end = front_end + "<br/>" + item.__repr__()
    return front_end


@app.route('/update_inventory')
def update_inventory():
    inventory.update_quality()
    front_end = "----------- Inventory right now -----------<br/>"
    for item in inventory.items:
        front_end = front_end + "<br/>" + item.__repr__()
    return front_end


@app.route('/update_inventory/<days>')
def update_inventory_days(days):
    inventory_of_days = Gildedrose([Normalitem("+5 Dexterity Vest", 10, 20), Agedbrie("Aged Brie", 2, 0), Normalitem("Elixir of the Mongoose", 5, 7), Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80), Sulfuras("Sulfuras, Hand of Ragnaros", -1, 80), Backstagepass("Backstage passes to a TAFKAL80ETC concert", 15, 20), Backstagepass("Backstage passes to a TAFKAL80ETC concert", 10, 49), Backstagepass("Backstage passes to a TAFKAL80ETC concert", 5, 49), Conjured("Conjured Mana Cake", 3, 6)])
    front_end = "----------- Update at Day " + days + " -----------<br/>"
    for day in range(1, int(days) + 1):
        inventory_of_days.update_quality()
    for item in inventory_of_days.items:
        front_end = front_end + "<br/>" + item.__repr__()
    return front_end


if __name__ == "__main__":
    app.run()
