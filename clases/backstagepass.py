from clases.normalitem import Normalitem


class Backstagepass(Normalitem):

    def update_quality(self):
        if self.sell_in > 10:
            self.quality += 1
        elif self.sell_in <= 10 and self.sell_in > 5:
            self.quality += 2
        else:
            self.quality += 3

        if self.sell_in < 0:
            self.quality = 0
        
        if self.quality > 50:
            self.quality = 50

        Normalitem.set_sellin(self)
        print(self.__repr__())
