bakery_dist = {}

details = input().split()
searched_products = input().split()

for element in range(0,len(details),2):
    key = details[element]
    value = int(details[element + 1])
    bakery_dist[key] = int(value)
for product in searched_products:
    if product in bakery_dist:
        print(f"We have {bakery_dist[product]} of {product} left")
    else:
        print(f"Sorry we don't have {product}")