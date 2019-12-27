from clases.updatable import Updatable
from clases.item import Item


class Normalitem(Item, Updatable):

    def set_sellin(self):
        self.sell_in -= 1
        normal_item = self.__repr__()
        return normal_item

    def update_quality(self):
        if (self.quality <= 50 or self.quality > 0) and self.sell_in >= 0:
            self.quality -= 1
        elif (self.quality <= 50 or self.quality > 0) and self.sell_in < 0:
            self.quality -= 2
        else:
            pass
        normal_item = self.__repr__()
        return normal_item
