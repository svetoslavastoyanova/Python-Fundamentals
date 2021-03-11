dict = {}
line = input()

while line != "stop":
    quantity = int(input())

    if line not in dict:
        dict[line] = 0

    dict[line] += quantity
    line = input()

for key, value in dict.items():
    print(f"{key} -> {value}")