line = input()
courses = {}

while line != "end":
    tokens = line.split(" : ")
    course = tokens[0]
    student = tokens[1]

    if course not in courses:
        courses[course] = []
    courses[course].append(student)

    line = input()

sorted_courses = dict(sorted(courses.items(), key=lambda x: -len(x[1])))

for key, value in sorted_courses.items():
    print(f"{key}: {len(value)}")
    for students in sorted(value):
        print(f"-- {students}")

