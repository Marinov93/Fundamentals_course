miner_dict = {}

command = input()
while command != 'stop':
    quantity = int(input())
    if command not in miner_dict:
        miner_dict[command] = 0
    miner_dict[command] += quantity

    command = input()

for resource , quantity in miner_dict.items():
    print(f"{resource} -> {quantity}")