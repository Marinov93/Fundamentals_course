products_dict = {}

while True:
    products_info = input()
    if products_info == 'buy':
        break
    products_info = products_info.split()
    for index in range(0, len(products_info), 3):
        product_name = products_info[index]
        product_price = float(products_info[index + 1])
        product_quantity = int(products_info[index + 2])
        if product_name not in products_dict:
            products_dict[product_name] = {'price': 0, 'quantity': 0}
        products_dict[product_name]['price'] = product_price
        products_dict[product_name]['quantity'] += product_quantity

for product_name, product_info in products_dict.items():
    total_cost = product_info['price'] * product_info['quantity']
    print(f"{product_name} -> {total_cost:.2f}")