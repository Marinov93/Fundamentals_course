courses = {}

while True:
    input_data = input()
    if input_data == 'end':
        break
    course_name, student_name = input_data.split(" : ")
    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)

for course_name, students in courses.items():
    print(f"{course_name}: {len(students)}")
    for student in students:
        print(f"-- {student}")
