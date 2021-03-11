line = input()

for i in range(len(line)):
    if line[i] == ":":
        word = line[i + 1]
        print(f":{word}")




