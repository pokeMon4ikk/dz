a = 1
items = []
b = int(input('Please enter number of items: '))
for i in range(b):
    name = input('Enter name of item: ')
    price = input('Enter price of item: ')
    quantity = input('Enter quantity of items: ')
    measure = input('Enter measure of item: ')
    items.append((a, {'name': name, 'price': price, 'quantity': quantity, 'measure': measure}))
    a = a + 1
print(items)
items_dict = {'name': [], 'price': [], 'quantity': [], 'measure': []}
for j in items:
    items_dict['name'].append(items[1]['name'])
    items_dict['price'].append(items[1]['price'])
    items_dict['quantity'].append(items[1]['quantity'])
    if items[1]['pc'] not in items_dict['pc']:
        items_dict['pc'].append(items[1]['pc'])
print(items_dict)
