from clases.gildedrose import Gildedrose


class Add_item(Gildedrose):
    def add_item(self, items):
        for item in items:
            self.items.append(item)
        print(self.items)
