students_dict = {}
courses_dict = {}

while True:
    students_info = input().split("-")
    if len(students_info) == 1:
        break
    elif len(students_info) == 2: # if elements in command are 2 or -> students name and banned
        username = students_info[0]
        del students_dict[username]
    else:
        username, language, points = students_info[0], students_info[1], int(students_info[2]) # split with index
        if username not in students_dict.keys():
            students_dict[username] = 0
        if students_dict[username] < points:
            students_dict[username] = points
        if language not in courses_dict.keys():
            courses_dict[language] = 0
        courses_dict[language] += 1

print("Results:")
for username, points in students_dict.items():
    print(f"{username} | {points}")

print("Submissions:")
for course , submissions in courses_dict.items():
    print(f"{course} - {submissions}")



