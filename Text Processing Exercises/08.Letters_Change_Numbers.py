position_lower = {chr(ele+97): ele+1 for ele in range(26)}
position_upper = {chr(ele+65): ele+1 for ele in range(26)}
result = 0
line = input().split()

for el in line:
        first_letter = el[0]
        number = int(el[1:-1])
        last_letter = el[-1]
        if first_letter.isupper():
            number /= position_upper[first_letter]
        elif first_letter.islower():
            number *= position_lower[first_letter]
        if last_letter.isupper():
            number -= position_upper[last_letter]
        elif last_letter.islower():
            number += position_lower[last_letter]
        result += number

print(f"{result:.2f}")


