from clases.updatable import Updatable
from clases.item import Item
from clases.normalitem import Normalitem

class Gildedrose:
    def __init__(self, Updatable):
        self.items = Updatable

    def get_items(self):
        list_of_items = []
        for item in Updatable.__subclasses__():
            list_of_items.append(item)
        return list_of_items

    def update_quality(self):
        list_of_items = Gildedrose.get_items(self)
        for item in list_of_items:
            item.update_quality(self)

