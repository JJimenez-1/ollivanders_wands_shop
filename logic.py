from main import *


def update_days(days_passed):
    updated_inventory = []
    acumulador = 0
    while acumulador < days_passed:
        for item in items:
            item.update_quality()
            updated_inventory.append(item.__repr__())
    return updated_inventory
