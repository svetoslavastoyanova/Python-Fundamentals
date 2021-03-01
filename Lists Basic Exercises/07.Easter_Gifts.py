gifts = input().split(" ")
command = input()

while command != "No Money":
    current = command.split(" ")

    if current[0] == "OutOfStock":
        gift = current[1]
        for i in range(len(gifts)):
            if gifts[i] == gift:
                gifts[i] = "None"

    elif current[0] == "Required":
        idx = int(current[2])
        if idx >= 0 and idx < len(gifts):
            gifts[idx] = current[1]

    elif current[0] == "JustInCase":
        gifts[-1] = current[1]

    command = input()

result = []
for gift in gifts:
    if gift != "None":
        result.append(gift)
print(" ".join(result))

