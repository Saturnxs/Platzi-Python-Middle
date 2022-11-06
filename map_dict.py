original_items = [
    {
        'product': 'Camisa',
        'price': 100
    },
    {
        'product': 'Zapatos',
        'price': 500
    },
    {
        'product': 'Lentes',
        'price': 450
    }
]

# Using the map function to iterate over the items list and return the price of each item.
prices = list(map(lambda item: item['price'], original_items))
print(prices) # [100, 500, 450]

# Iterating over the items list and returning the product of each item.
products = list(map(lambda item: item['product'], original_items))
print(products) # ['Camisa', 'Zapatos', 'Lentes']


# INMUTABLE MAP

# Creating a new item and adding a new key to it.
def add_taxes(item):
    new_item = item.copy()
    new_item['taxes'] = new_item['price'] * .13
    return new_item

# Iterating over the items list and returning a new list with the new items.
new_items = list(map(add_taxes, original_items))
print(new_items) 
# [
#     {'product': 'Camisa', 'price': 100, 'taxes': 13.0},
#     {'product': 'Zapatos', 'price': 500, 'taxes': 65.0},
#     {'product': 'Lentes', 'price': 450, 'taxes': 58.5}
# ]
print(original_items) # Origianl list is the same
# [
#     {'product': 'Camisa', 'price': 100},
#     {'product': 'Zapatos', 'price': 500},
#     {'product': 'Lentes', 'price': 450}
# ]



# MUTABLE MAP


# Adding a new key to the item dictionary.
def add_taxes(item):
    item['taxes'] = item['price'] * .13
    return item


# Iterating over the items list and returning a new list with the new items.
new_items = list(map(add_taxes, original_items))
print(new_items) 
# [
#     {'product': 'Camisa', 'price': 100, 'taxes': 13.0},
#     {'product': 'Zapatos', 'price': 500, 'taxes': 65.0},
#     {'product': 'Lentes', 'price': 450, 'taxes': 58.5}
# ]
print(original_items) # Modified original list
# [
#     {'product': 'Camisa', 'price': 100, 'taxes': 13.0},
#     {'product': 'Zapatos', 'price': 500, 'taxes': 65.0},
#     {'product': 'Lentes', 'price': 450, 'taxes': 58.5}
# ]