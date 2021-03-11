line = input().lower().split()
dict = {}
while True:

    for i in range(0, len(line), 2):
        if line == " ":
            continue
        number = int(line[i])
        material = line[i + 1]

        if material not in dict:
            dict[material] = 0
        dict[material] += number

    line = input()
print(dict)



