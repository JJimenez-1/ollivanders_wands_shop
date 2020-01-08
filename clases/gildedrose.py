from clases.updatable import Updatable
from clases.item import Item
from clases.normalitem import Normalitem
from clases.agedbrie import Agedbrie
from clases.backstagepass import Backstagepass
from clases.conjured import Conjured
from clases.sulfuras import Sulfuras


class Gildedrose:
    def __init__(self, items):
        self.items = items

    def add_item(items):
        list_of_items = []
        for item in items:
            try:
                if (item.quality > 50 or item.quality < 0) and item.name != "Sulfuras, Hand of Ragnaros":
                    raise ValueError
            except ValueError:
                print(item.name + ' no cumple los requisitos para entrar en la tienda.')
            else:
                list_of_items.append(item)
        return list_of_items

    def get_items(self):
        inventory = []
        for item in self.items:
            inventory.append(item.__repr__())
        return inventory

    def update_quality(self):
        for item in self.items:
            item.update_quality()
