import json


def count_cities():
    str = 'Ahmedabad'
    k = 0
    with open('cities.json', 'r') as f:
        items = json.load(f)

    for item in items:
        if item['c'].lower() == str.lower():
            k = k + 1

    return k