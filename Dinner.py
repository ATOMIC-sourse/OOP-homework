from Cookbook import cook_book
from pprint import pprint

with open("Cookbook.py", 'r', encoding='utf-8') as f:
    data = f.read()

def get_shop_list_by_dishes(dishes, person_count):
    list1 = []
    list2 = []
    list3 = []
    for dish in dishes:
        if dish in cook_book:
            for i in cook_book.get(dish):
                if i['ingredient_name'] not in list1:
                    list1.append(i['ingredient_name'])
                list2.append({'measure': i['measure'], 'quantity': i['quantity'] * person_count})
    list3.append({name: age for name, age in zip(list1, list2)})
    for a in list3:
        print(a)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)