from clases.gildedrose import *


dexterity = Normalitem("+5 Dexterity Vest", 10, 20)
mongoose = Normalitem("Elixir of the Mongoose", 5, 7)
agedbrie = Agedbrie("Aged Brie", 2, 0)
sulfuras = Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80)
sulfuras_two = Sulfuras("Sulfuras, Hand of Ragnaros", -1, 80)
backstage = Backstagepass("Backstage passes to a TAFKAL80ETC concert", 15, 20)
backstage_two = Backstagepass("Backstage passes to a TAFKAL80ETC concert", 10, 49)
backstage_three = Backstagepass("Backstage passes to a TAFKAL80ETC concert", 5, 49)
conjured = Conjured("Conjured Mana Cake", 3, 6)

items = Gildedrose.add_item([dexterity, agedbrie, mongoose, sulfuras, sulfuras_two, backstage, backstage_two, backstage_three, conjured])
inventario = Gildedrose(items)


if __name__ == "__main__":
    print("-------------- Inventory at this moment --------------")
    inventario.get_items()
    print("-------------- Inventory updated --------------")
    inventario.update_quality()
