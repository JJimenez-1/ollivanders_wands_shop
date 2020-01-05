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

    def get_items(self):
        for item in self.items:
            print(item.__repr__())

    def update_quality(self):
        for item in self.items:
            item.update_quality()
