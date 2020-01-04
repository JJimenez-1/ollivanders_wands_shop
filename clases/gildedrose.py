from clases.updatable import Updatable
from clases.item import Item
from clases.normalitem import Normalitem
from clases.agedbrie import Agedbrie
from clases.backstagepass import Backstagepass
from clases.conjured import Conjured
from clases.sulfuras import Sulfuras


class Gildedrose:
    def __init__(self, Updatable, Normalitem):
        self.items = []

    def get_items(self):
        return self.items.__repr__()

    def update_quality(self):
        klass = Gildedrose.get_items(self)
        for item in klass:
            item.update_quality(self)
