line = input()

i = 0
rage_str = ""
result = ""
while i < len(line):
    ch = line[i]

    if ch.isdigit():
        count_str = ch

        if i + 1 < len(line) and line[i + 1].isdigit():
            count_str += line[i + 1]
            i += 1

        count = int(count_str)
        result += rage_str.upper() * count

        rage_str = ""

    else:
        rage_str += ch

    i += 1

symbols = len(set(result))
print(f"Unique symbols used: {symbols}")
print(result)