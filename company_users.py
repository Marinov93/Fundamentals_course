company_users_dict = {}

while True:
    command = input()
    if command == 'End':
        break
    elements = command.split(" -> ")
    company_name, users_id = elements[0], elements[1]
    if company_name not in company_users_dict:
        company_users_dict[company_name] = []
    if users_id not in company_users_dict[company_name]:
        company_users_dict[company_name].append(users_id)

for company_name, users_id in company_users_dict.items():
    print(f"{company_name}")
    for users in users_id:
        print(f"-- {users}")
