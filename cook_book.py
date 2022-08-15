import json

keys = ['ingredient_name', 'quantity', 'measure']
cook_book = {}

with open('recipes.txt', encoding='utf-8') as f:
    lines = []
    for line in f:
        line = line.strip()
        if line:
            lines.append(line)
    lines = iter(lines)
    for dish in lines:
        cook_book_dish = []
        persons = next(lines)
        for num in range(int(persons)):
            ingredient_line = next(lines)
            ingredients = ingredient_line.split(' | ')
            cook_book_dish.append({'ingredient_name': ingredients[0], 'quantity': int(ingredients[1]), 'measure': ingredients[2]})
            cook_book[dish] = cook_book_dish
        continue

# print(cook_book)         

print(json.dumps(cook_book, indent=2, ensure_ascii=False))


def get_shop_list_by_dishes(dishes, persons):
    shop_list = {}
    for dish in dishes:
        for dishes in cook_book[dish]:
            shop_list_item = dict(dishes)
            shop_list_item['quantity'] *= persons
            if shop_list_item['ingredient_name'] not in shop_list:
                shop_list[shop_list_item['ingredient_name']] = shop_list_item
            else:
                shop_list[shop_list_item['ingredient_name']]['quantity'] += shop_list_item['quantity']
    return shop_list

def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print(f"{shop_list_item['ingredient_name']}, {shop_list_item['quantity']}, {shop_list_item['measure']}")

def add_shop_list():
    persons = int(input('Введите количество персон: '))
    dishes = input('Введите блюда через запятую: ').capitalize().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, persons)
    print_shop_list(shop_list)
    
add_shop_list()