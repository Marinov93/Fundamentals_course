students_dict = {}

number_of_pairs = int(input())

for student in range(number_of_pairs):
    students_info = input()
    students_grade = float(input())
    if students_info not in students_dict:
        students_dict[students_info] = []
    students_dict[students_info].append(students_grade)

for student, grade in students_dict.items():
    if sum(grade) / len(grade) >= 4.50:
        print(f"{student} -> {sum(grade) / len(grade):.2f}")
