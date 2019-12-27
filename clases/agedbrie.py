from normalitem import Normalitem


class Agedbrie(Normalitem):

    def update_quality(self):
        if self.quality < 50 and self.quality >= 0 and self.sell_in >= 0:
            self.quality += 1
        elif self.quality < 50 and self.quality >= 0 and self.sell_in < 0:
            self.quality += 2
        else:
            pass

        if self.quality > 50:
            self.quality = 50
        aged_brie = self.__repr__()
        return aged_brie
