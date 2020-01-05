from clases.updatable import Updatable
from clases.item import Item


class Normalitem(Item, Updatable):

    def set_sellin(self):
        self.sell_in -= 1

    def update_quality(self):
        if (self.quality <= 50 or self.quality > 0) and self.sell_in >= 0:
            self.quality -= 1
        elif (self.quality <= 50 or self.quality > 0) and self.sell_in < 0:
            self.quality -= 2
        else:
            pass

        if self.quality < 0:
            self.quality = 0

        Normalitem.set_sellin(self)
        print(self.__repr__())
