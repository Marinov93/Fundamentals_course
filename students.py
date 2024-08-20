course_search = ''

students_dict = []

while True:

    students_info = input()
    if ":" not in students_info:
        course_search = students_info
        break

    name, id_, course_name = students_info.split(":")
    students_dict.append({'name': name, 'id': id_, 'course': course_name})
for student in students_dict:
    if course_search.startswith(student['course'][0:3]):
        print(f"{student['name']} - {student['id']}")
