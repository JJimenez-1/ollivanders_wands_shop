from clases.normalitem import Normalitem


class Sulfuras(Normalitem):

    def set_sellin(self):
        self.sell_in == self.sell_in

    def update_quality(self):
        self.quality == self.quality

        Sulfuras.set_sellin(self)
        return self.__repr__()

