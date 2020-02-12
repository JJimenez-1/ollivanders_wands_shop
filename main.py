from domain.gildedrose import *


def main(days_passed):
    inventory = Gildedrose([Normalitem("+5 Dexterity Vest", 10, 20),
                            Agedbrie("Aged Brie", 2, 0),
                            Normalitem("Elixir of the Mongoose", 5, 7),
                            Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80),
                            Sulfuras("Sulfuras, Hand of Ragnaros", -1, 80),
                            Backstagepass("Backstage passes to a TAFKAL80ETC concert", 15, 20),
                            Backstagepass("Backstage passes to a TAFKAL80ETC concert", 10, 49),
                            Backstagepass("Backstage passes to a TAFKAL80ETC concert", 5, 49),
                            Conjured("Conjured Mana Cake", 3, 6)])
    inventory.add_item()
    actual_inventory = inventory.get_items()
    print("----------- Inventory right now -----------")
    for item in actual_inventory:
        print(item)
    for day in range(1, days_passed + 1):
        print("---------- Inventory updated: Day " + str(day) + " ----------")
        inventory.update_quality()
        for item in inventory.items:
            print(item)
    list_of_items_updated = []
    for item in inventory.items:
        list_of_items_updated.append(item.__repr__())
    return list_of_items_updated


if __name__ == "__main__":
    main(30)
