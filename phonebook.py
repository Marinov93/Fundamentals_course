phonebook = {}

while True:
    entry_info = input()
    if "-" not in entry_info:
        break
    name, phone_number = entry_info.split("-")
    phonebook[name] = phone_number

searched = int(entry_info)
for index in range(searched):
    name = input()
    if name not in phonebook:
        print(f"Contact {name} does not exist.")
    else:
        print(f"{name} -> {phonebook[name]}")
