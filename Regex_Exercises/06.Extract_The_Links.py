import re
regex = r"(www)\.(([a-zA-Z\d]+)|(([a-zA-Z\d]+)?\-[a-zA-z\d]+)+)(\.[a-z]+)+"
line = input()
while True:

    if not line:
        break

    matches = re.finditer(regex, line)
    for match in matches:
        print(match[0])

    line = input()