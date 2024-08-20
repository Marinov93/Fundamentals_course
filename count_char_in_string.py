chars_dict = {}

space_removal = [char for char in input() if char != " "]

for word in space_removal:
    if word not in chars_dict.keys():
        chars_dict[word] = 0
    chars_dict[word] += 1

for element,value in chars_dict.items():
    print(f"{element} -> {value}")
