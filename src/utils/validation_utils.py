from . import json_utils

def validate_input(input_str, input_file):
    items = json_utils.get_items_from_json(input_file)
    input_chars = list(input_str)
    for i in input_chars:
        if i not in items:
            raise Exception(f"Invalid input characters. Allowed characters are: {items}")
    return input_str
