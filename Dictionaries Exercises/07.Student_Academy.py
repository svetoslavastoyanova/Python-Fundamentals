pair_of_rows = int(input())

students = {}

for i in range(pair_of_rows):
    student_name = input()
    student_grade = float(input())

    if student_name not in students:
        students[student_name] = []

    students[student_name].append(student_grade)

students_average = {key: sum(value)/len(value) for (key, value) in students.items() if sum(value)/len(value) >= 4.5}
students_average = dict(sorted(students_average.items(), key=lambda x: x[1], reverse=True))

for key, value in students_average.items():
    print(f"{key} -> {value:.2f}")




