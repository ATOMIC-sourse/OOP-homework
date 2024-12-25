cook_book = {}

with open('Cookbook.py', 'rt', encoding="utf-8") as file:
    for l in file:
        dish_name = l.strip()
        new_list = []
        count = file.readline()
        for i in range(int(count)):
            dish_ing = file.readline()
            ingredient_name, quantity, measure = dish_ing.strip().split(' | ')
            new_list.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            dep = {dish_name: new_list}
        separate = file.readline()
        cook_book.update(dep)
        print(separate)

# print(f'cook_book = {cook_book}')

# def list_of_stores_with_ingredients(dishes, person_count):
#     total = {}
#     for dish in dishes:
#         if dish in cook_book:
#             for exist in cook_book[dish]:
#                 total
#                 {'measure': cook_book['measure'], 'quantity': (int(cook_book['quantity']) * int(person_count)),}
#     return total
#
#
# list_of_stores_with_ingredients(["Омлет"], 2)
