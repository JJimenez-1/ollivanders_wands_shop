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
