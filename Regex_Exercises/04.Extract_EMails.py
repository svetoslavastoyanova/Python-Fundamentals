import re
line = input()

regex = r"( |^)([a-zA-Z0-9]+((\.|\-_)?[a-zA-Z0-9]+)*@([a-zA-Z|\-]+\.[a-zA-Z]+)(\.[a-zA-Z]+)*)"

matches = re.finditer(regex, line)
for match in matches:
    print(match[2])




