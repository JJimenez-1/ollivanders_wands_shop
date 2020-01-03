from clases.item import Item
from clases.normalitem import Normalitem
from clases.updatable import Updatable
from clases.agedbrie import Agedbrie
from clases.sulfuras import Sulfuras
from clases.backstagepass import Backstagepass
from clases.conjured import Conjured
from clases.gildedrose import Gildedrose


def test_class_normalitem_works():
    normal_item = Normalitem("potatoe", 10, 8)
    item_sellin_updated = normal_item.set_sellin() and normal_item.update_quality()
    assert item_sellin_updated == "potatoe, 9, 7"


def test_class_normalitem_setsellin_negative():
    normal_item = Normalitem("carrot", -1, 8)
    item_sellin_update = normal_item.set_sellin() and normal_item.update_quality()
    assert item_sellin_update == "carrot, -2, 6"


def test_class_normalitem_quality_to_zero():
    normal_item = Normalitem("watermelon", -1, 1)
    item_sellin_update = normal_item.set_sellin() and normal_item.update_quality()
    assert item_sellin_update == "watermelon, -2, 0"


def test_class_Agedbrie_works():
    aged_brie = Agedbrie("apple", -25, 48)
    item_sellin_update = aged_brie.set_sellin() and aged_brie.update_quality()
    assert item_sellin_update == "apple, -26, 50"


def test_class_Agedbrie_quality_to_50():
    aged_brie = Agedbrie("apple", -25, 49)
    item_sellin_update = aged_brie.set_sellin() and aged_brie.update_quality()
    assert item_sellin_update == "apple, -26, 50"


def test_class_Sulfuras_works():
    sulfuras = Sulfuras("Sulfuras", 0, 50)
    item_update = sulfuras.set_sellin() and sulfuras.update_quality()
    assert item_update == "Sulfuras, 0, 50"


def test_class_Backstagepass_works():
    backstage_pass = Backstagepass("Backstagepass", 3, 10)
    item_update = backstage_pass.set_sellin() and backstage_pass.update_quality()
    assert item_update == "Backstagepass, 2, 13"


def test_class_Conjured_works():
    conjured = Conjured("Conjured", 3, 10)
    item_update = conjured.set_sellin() and conjured.update_quality()
    assert item_update == "Conjured, 2, 8"


def test_main():
    items = [
                Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
                Item(name="Aged Brie", sell_in=2, quality=0),
                Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
                Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
                Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
                Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
                Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
                Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
                Item(name="Conjured Mana Cake", sell_in=3, quality=6),
                ]
    items_updated = Gildedrose.update_quality(items)
    list_of_items = self.__repr__()
    return list_of_items


if __name__ == "__main__":
    assert test_main() == True
