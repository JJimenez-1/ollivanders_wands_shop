from clases.item import Item
from clases.normalitem import Normalitem
from clases.updatable import Updatable
from clases.agedbrie import Agedbrie

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
    item_sellin_update = normal_item.set_sellin() and aged_brie.update_quality()
    assert item_sellin_update == "apple, -26, 50"


def test_class_Agedbrie_quality_to_50():
    aged_brie = Agedbrie("apple", -25, 49)
    item_sellin_update = Normalitem.set_sellin() and aged_brie.update_quality()
    assert item_sellin_update == "apple, -26, 50"
