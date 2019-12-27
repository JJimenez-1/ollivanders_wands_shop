from clases.item import Item
from clases.normalitem import Normalitem
from clases.updatable import Updatable


def test_class_normalitem_works():
    normal_item = Normalitem("potatoe", 10, 8)
    item_sellin_updated = normal_item.set_sellin() and normal_item.update_quality()
    assert item_sellin_updated == "potatoe, 9, 7"


def test_class_normalitem_setsellin_negative():
    normal_item = Normalitem("carrot", -1, 8)
    item_sellin_update = normal_item.set_sellin() and normal_item.update_quality()
    assert item_sellin_update == "carrot, -2, 6"
