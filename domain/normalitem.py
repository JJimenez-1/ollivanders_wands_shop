from domain.updatable import Updatable
from domain.item import Item


class Normalitem(Item, Updatable):

    def set_sellin(self):
        self.sell_in -= 1

    def update_quality(self):
        Normalitem.set_sellin(self)
        if (self.quality <= 50 or self.quality > 0) and self.sell_in >= 0:
            self.quality -= 1
        elif (self.quality <= 50 or self.quality > 0) and self.sell_in < 0:
            self.quality -= 2
        else:
            pass
        if self.quality < 0:
            self.quality = 0
