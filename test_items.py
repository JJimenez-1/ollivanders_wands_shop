from clases.item import Item
from clases.normalitem import Normalitem
from clases.updatable import Updatable


def test_clase_funciona_correctamente():
    assert Normalitem.set_sellin("potatoe", 10, 8) == ("potatoe", 9, 7)
