first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
total_people_count = int(input())
people_answered_per_hour = first_employee + second_employee + third_employee
counter = 0

while total_people_count > 0:
    counter += 1
    total_people_count -= people_answered_per_hour

    if counter % 4 == 0:
        counter += 1

print(f"Time needed: {counter}h.")


