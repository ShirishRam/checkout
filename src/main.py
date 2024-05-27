"""
Main program for checkout pricing logic
"""
from utils import json_utils, validation_utils


UNIT_PRICE_DICT = json_utils.get_unit_prices_from_json('unit_price.json')
SPECIAL_PRICE_DICT = json_utils.get_special_prices_from_json('special_price.json')

def pricing_logic(item, qty):
    for sp_item, (sp_qty, sp) in SPECIAL_PRICE_DICT.items():
        if (sp_item == item):
            if (qty % sp_qty == 0): # if item qty is a multiple of qty defined for special price then use below formula
                return int(sp * qty / sp_qty)
            elif (qty > sp_qty): # if item qty is more than qty defined for special price then use below formula
                return int(sp * int(qty / sp_qty) + UNIT_PRICE_DICT[item] * (qty % sp_qty))

    # no special price rule for the item, then calculate based on unit price
    return UNIT_PRICE_DICT[item] * qty

def calculate_total_price(items_str):
    items_list = list(items_str)
    total_price = 0
    item_quantities_dict = {}

    for item in items_list:
        item_quantities_dict[item] = item_quantities_dict.get(item, 0) + 1

    for item, qty in item_quantities_dict.items():
        item_price = pricing_logic(item, qty)
        total_price += item_price

    print(total_price)

if __name__ == '__main__':
    input_str = input("Please provide the checkout items input:\n")
    valid_items_str = validation_utils.validate_input(input_str, 'unit_price.json')
    calculate_total_price(valid_items_str)
