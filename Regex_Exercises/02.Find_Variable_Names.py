import re
regex = r"\b_{1}([A-Za-z0-9]+)\b"
list = []
line = input()
matches = re.finditer(regex, line)

for match in matches:
    list.append(match[1])

print(",".join(list), end="")






















