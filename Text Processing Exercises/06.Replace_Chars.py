line = input()

for index in range(len(line)):
    if index + 1 == len(line):
        print(line[index], end="")
        break

    if line[index] != line[index + 1]:
        print(line[index], end="")




