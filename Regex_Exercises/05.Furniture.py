import re
line = input()
price = []
furniture = []
regex = r"\>{2}([a-zA-Z]+)\<{2}((?:\d+(?:\.\d*)?|\.\d+))(\!{1})([0-9]+)"

while line != "Purchase":
    matches = re.finditer(regex, line)
    for match in matches:
        furniture.append(match[1])
        product = float(match[2])
        quantity = float(match[4])
        result = product * quantity
        price.append(result)
    line = input()

print(f"Bought furniture:")
for f in furniture:
    print(f)
print(f"Total money spend: {sum(price):.2f}")






