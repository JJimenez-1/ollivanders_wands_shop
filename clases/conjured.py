from clases.normalitem import Normalitem


class Conjured(Normalitem):

    def update_quality(self):
        if (self.quality <= 50 or self.quality > 0) and self.sell_in >= 0:
            self.quality -= 2
        elif (self.quality <= 50 or self.quality > 0) and self.sell_in < 0:
            self.quality -= 4
        else:
            pass

        if self.quality < 0:
            self.quality = 0

        Normalitem.set_sellin(self)
        return self.__repr__()
