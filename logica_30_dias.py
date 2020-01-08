from main import *


def update_days(days_passed):
    list_of_items = []
    acumulador = 0
    while acumulador < days_passed:
        inventory.update_quality()
        acumulador += 1
    for item in items_accepted:
            list_of_items.append(item.__repr__())
    return list_of_items
