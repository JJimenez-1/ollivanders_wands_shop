from domain.updatable import Updatable
from domain.item import Item
from domain.normalitem import Normalitem
from domain.agedbrie import Agedbrie
from domain.backstagepass import Backstagepass
from domain.conjured import Conjured
from domain.sulfuras import Sulfuras


class Gildedrose:
    def __init__(self, items):
        self.items = items

    def add_item(self):
        for item in self.items:
            try:
                if (item.quality > 50 or item.quality < 0) and item.name != "Sulfuras, Hand of Ragnaros":
                    raise ValueError
            except ValueError:
                print(item.name + ' no cumple los requisitos para entrar en la tienda.')
                self.items.remove(item)
            else:
                pass

    def get_items(self):
        return self.items

    def update_quality(self):
        for item in self.items:
            item.update_quality()
