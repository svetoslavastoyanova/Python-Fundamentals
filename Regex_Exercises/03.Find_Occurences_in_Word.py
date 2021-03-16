import re
line = input()
word = input()

regex = rf"\b{word}\b"

matches = re.findall(regex, line, re.IGNORECASE)
print(len(matches))

