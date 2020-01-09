from main import *


def test_class_normalitem_works():
    normal_item = Normalitem("potatoe", 10, 8)
    normal_item.update_quality()
    normal_item = normal_item.__repr__()
    assert normal_item == "potatoe, 9, 7"


def test_class_normalitem_setsellin_negative():
    normal_item = Normalitem("carrot", -1, 8)
    normal_item.update_quality()
    normal_item = normal_item.__repr__()
    assert normal_item == "carrot, -2, 6"


def test_class_normalitem_quality_to_zero():
    normal_item = Normalitem("watermelon", -1, 1)
    normal_item.update_quality()
    normal_item = normal_item.__repr__()
    assert normal_item == "watermelon, -2, 0"


def test_class_normalitem_quality_not_negative():
    normal_item = Normalitem("watermelon", -1, 0)
    normal_item.update_quality()
    normal_item = normal_item.__repr__()
    assert normal_item == "watermelon, -2, 0"


def test_class_Agedbrie_works():
    aged_brie = Agedbrie("apple", -25, 48)
    aged_brie.update_quality()
    aged_brie = aged_brie.__repr__()
    assert aged_brie == "apple, -26, 50"


def test_class_Agedbrie_quality_to_50():
    aged_brie = Agedbrie("apple", -25, 49)
    aged_brie.update_quality()
    aged_brie = aged_brie.__repr__()
    assert aged_brie == "apple, -26, 50"


def test_class_Agedbrie_quality_not_more_than_50():
    aged_brie = Agedbrie("apple", -25, 50)
    aged_brie.update_quality()
    aged_brie = aged_brie.__repr__()
    assert aged_brie == "apple, -26, 50"


def test_class_Sulfuras_works():
    sulfuras = Sulfuras("Sulfuras", 0, 50)
    sulfuras.update_quality()
    sulfuras = sulfuras.__repr__()
    assert sulfuras == "Sulfuras, 0, 50"


def test_class_Backstagepass_works():
    backstage_pass = Backstagepass("Backstagepass", 3, 10)
    backstage_pass.update_quality()
    backstage_pass = backstage_pass.__repr__()
    assert backstage_pass == "Backstagepass, 2, 13"


def test_class_Backstagepass_sellin_between_5_and_0():
    backstage_pass = Backstagepass("Backstagepass", 5, 10)
    backstage_pass.update_quality()
    backstage_pass = backstage_pass.__repr__()
    assert backstage_pass == "Backstagepass, 4, 13"


def test_class_Backstagepass_negative_sellin():
    backstage_pass = Backstagepass("Backstagepass", 0, 10)
    backstage_pass.update_quality()
    backstage_pass = backstage_pass.__repr__()
    assert backstage_pass == "Backstagepass, -1, 0"


def test_class_Conjured_works():
    conjured = Conjured("Conjured", 3, 10)
    conjured.update_quality()
    conjured = conjured.__repr__()
    assert conjured == "Conjured, 2, 8"


def test_class_Conjured_negative_sellin():
    conjured = Conjured("Conjured", -3, 10)
    conjured.update_quality()
    conjured = conjured.__repr__()
    assert conjured == "Conjured, -4, 6"


def test_class_Gildedrose_Normalitem():
    gildedrose = Gildedrose([Normalitem("Phoneix", 4, 33)])
    gildedrose.update_quality()
    for item in gildedrose.items:
        item_updated = item.__repr__()
    assert item_updated == "Phoneix, 3, 32"


def test_class_Gildedrose_Conjured():
    gildedrose = Gildedrose([Conjured("Conjured dark mana", 1, 20)])
    gildedrose.update_quality()
    for item in gildedrose.items:
        item_updated = item.__repr__()
    assert item_updated == "Conjured dark mana, 0, 18"


def test_class_Gildedrose_Agedbrie():
    gildedrose = Gildedrose([Agedbrie("Agedbrie", -2, 43)])
    gildedrose.update_quality()
    for item in gildedrose.items:
        item_updated = item.__repr__()
    assert item_updated == "Agedbrie, -3, 45"


def test_class_Gildedrose_Backstagepass():
    gildedrose = Gildedrose([Backstagepass("Backstagepass", 0, 43)])
    gildedrose.update_quality()
    for item in gildedrose.items:
        item_updated = item.__repr__()
    assert item_updated == "Backstagepass, -1, 0"


def test_class_Gildedrose_Sulfuras():
    gildedrose = Gildedrose([Sulfuras("Sulfuras, Hand of Ragnaros", -10, 100)])
    gildedrose.update_quality()
    for item in gildedrose.items:
        item_updated = item.__repr__()
    assert item_updated == "Sulfuras, Hand of Ragnaros, -10, 100"


def test_class_Gildedrose_add_item_works():
    gildedrose = Gildedrose([Normalitem("Dragees", 10, 54)])
    gildedrose.add_item()
    assert gildedrose.items == []

