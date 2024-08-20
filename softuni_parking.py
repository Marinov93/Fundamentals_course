parking_slot = {}
number_of_commands = int(input())

for command in range(number_of_commands):
    name_command = input().split()
    if name_command[0] == 'register':
        username, license_plate_number = name_command[1], name_command[2]
        if username in parking_slot.keys():
            print(f"ERROR: already registered with plate number {license_plate_number}")
        else:
            parking_slot[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
    elif name_command[0] == 'unregister':
        username = name_command[1]
        if username not in parking_slot.keys():
            print(f"ERROR: user {username} not found")
        else:
            del parking_slot[username]
            print(f"{username} unregistered successfully")

for username, license_plate_number in parking_slot.items():
    print(f"{username} => {license_plate_number}")
