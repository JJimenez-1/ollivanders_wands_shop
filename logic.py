from main import *


def update_days(days_passed):
    acumulador = 0
    updated_items = []
    while acumulador < days_passed:
        updated_items = inventory.update_quality()
        acumulador += 1
    return updated_items
