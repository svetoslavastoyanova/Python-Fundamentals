
divisor = int(input())
bound = int(input())
max = - 100000000
current_number = 0
for number in range(divisor, bound + 1):
    if number % divisor == 0 and number <= bound and number >= 0:
        current_number += 1
        if number > max:
            max = number
            current_number = max

print(current_number)