countries = input().split(", ")
capitals = input().split(", ")

matched_list = {countries[index]:capitals[index] for index in range(len(capitals))}

for countries,capitals in matched_list.items():
    print(f"{countries} -> {capitals}")