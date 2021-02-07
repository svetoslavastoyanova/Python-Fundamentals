lines = int(input())
sum = 0
for a in range(1, lines + 1):
    letters = input()
    new_letter = ord(letters)
    sum += new_letter
print(f"The sum equals: {sum}")


