import json

def get_unit_prices_from_json(file_name):
    f = open(file_name)
    item_prices_json = json.load(f)
    unit_price_dict = {}

    for i in item_prices_json:
        unit_price_dict[i['item']] = i['price']

    f.close()
    return unit_price_dict

def get_special_prices_from_json(file_name):
    f = open(file_name)
    item_special_prices_json = json.load(f)
    special_price_dict = {}

    for i in item_special_prices_json:
        special_price_dict[i['item']] = (i['special_price_qty'], i['special_price'])

    f.close()
    return special_price_dict

def get_items_from_json(file_name):
    f = open(file_name)
    item_prices_json = json.load(f)
    items_dict = []

    for i in item_prices_json:
        items_dict.append(i['item'])

    f.close()
    return items_dict
