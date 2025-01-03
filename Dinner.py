from pprint import pprint

def read_cook_book(file):
    cookbook = {}
    with open(file, "r", encoding="utf-8") as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                file.readline().strip()
                break

            ingredient_count = int(file.readline().strip())
            ingredients = []

            for i in range(ingredient_count):
                ingredient_line = file.readline().strip()
                ingredient_name, quantity, measure = ingredient_line.split(" | ")
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })

            cookbook[dish_name] = ingredients

    return cookbook

cook_book = read_cook_book('recipes.txt')


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

get_shop_list_by_dishes(['Запеченный картофель','Омлет'], 2)