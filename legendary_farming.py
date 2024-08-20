# shadowmourne = 250 shards
# valany = 250 fragments
# dragonwarth = 250 motes

needed_materials = {"shards": 0, "fragments": 0, "motes": 0}
legendary_item_obtained = False
while not legendary_item_obtained:
    materials = input().split()
    for index in range(0, len(materials), 2):
        value = int(materials[index])
        key = materials[index + 1].lower()
        if key not in needed_materials.keys():
            needed_materials[key] = 0
        needed_materials[key] += value
        if needed_materials["shards"] >= 250:
            needed_materials["shards"] -= 250
            print("Shadowmourne obtained!")
            legendary_item_obtained = True
        elif needed_materials["fragments"] >= 250:
            needed_materials["fragments"] -= 250
            print("Valanyr obtained!")
            legendary_item_obtained = True
        elif needed_materials["motes"] >= 250:
            needed_materials["motes"] -= 250
            print("Dragonwrath obtained!")
            legendary_item_obtained = True
        if legendary_item_obtained:
            break

for element, quantity in needed_materials.items():
    print(f"{element}: {quantity}")
