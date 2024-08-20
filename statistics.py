products_dict = {}

command = input()
while command != 'statistics':
    key, value = command.split(":")
    if key not in products_dict:
        products_dict[key] = 0
    products_dict[key] += int(value)
    command = input()


print("Products in stock:")
for key,value in products_dict.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(products_dict)}")
print(f"Total Quantity: {sum(products_dict.values())}")
