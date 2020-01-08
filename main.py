from clases.gildedrose import *


dexterity = Normalitem("+5 Dexterity Vest", 10, 20)
mongoose = Normalitem("Elixir of the Mongoose", 5, 7)
aged_brie = Agedbrie("Aged Brie", 2, 0)
sulfuras = Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80)
sulfuras_two = Sulfuras("Sulfuras, Hand of Ragnaros", -1, 80)
backstage = Backstagepass("Backstage passes to a TAFKAL80ETC concert", 15, 20)
backstage_two = Backstagepass("Backstage passes to a TAFKAL80ETC concert", 10, 49)
backstage_three = Backstagepass("Backstage passes to a TAFKAL80ETC concert", 5, 49)
conjured_item = Conjured("Conjured Mana Cake", 3, 6)

items_accepted = Gildedrose.add_item([dexterity, aged_brie, mongoose, sulfuras, sulfuras_two, backstage, backstage_two, backstage_three, conjured_item])
inventory = Gildedrose(items_accepted)


if __name__ == "__main__":
    print("----------- Inventory right now -----------")
    inventory.get_items()
    for item in items_accepted:
        print(item)
    print("----------- Inventory updated -----------")
    inventory.update_quality()
    for item in items_accepted:
        print(item)
