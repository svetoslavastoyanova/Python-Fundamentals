import re
regex = r"\d+"

while True:
    line = input()
    if not line:
        break

    matches = re.findall(regex, line)
    for match in matches:
        print(match, end=" ")


