from Cookbook import cook_book
from pprint import pprint

with open("Cookbook.py", 'r', encoding='utf-8') as f:
    data = f.read()

def get_shop_list_by_dishes(dishes, person_count):
    dinner = dict
    for dish in dishes:
        print(dish)
        print(list(cook_book.keys()))
        if dish in cook_book.keys():
            print([0])
            dinner.update(cook_book.get(dish))

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

# first_plate = cook_book['Омлет']
# for i in first_plate:
#     pprint(i)

# dinner.update(cook_book['Омлет'])
# pprint(first_plate)