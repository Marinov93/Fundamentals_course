bakery_dist = {}

details = input().split()
for element in range(0,len(details), 2):
    key = details[element]
    value = details[element + 1]
    bakery_dist[key] = int(value)
print(bakery_dist)