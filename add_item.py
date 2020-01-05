def add_item(items):
    list_of_items = []
    for item in items:
        try:
            if item.quality > 50:
                raise ValueError
        except ValueError:
            print(item.name + ' no cumple los requisitos para entrar en la tienda.')
        else:
            list_of_items.append(item)

    return list_of_items
