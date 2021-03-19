weapon_name = input().split("|")


def right(index):
    if 0 <= index + 1 < len(weapon_name) and 0 <= index < len(weapon_name):
        weapon_name[index], weapon_name[index + 1] = weapon_name[index + 1], weapon_name[index]


def left(index):
    if 0 <= index - 1 < len(weapon_name) and 0 <= index < len(weapon_name):
        weapon_name[index - 1], weapon_name[index] = weapon_name[index], weapon_name[index - 1]


def even():
    res = ""
    for i in range(len(weapon_name)):
        if i % 2 == 0:
            res += f"{weapon_name[i]} "
    print(res)


def odd():
    res = ""
    for i in range(len(weapon_name)):
        if i % 2 != 0:
            res += f"{weapon_name[i]} "
    print(res)


command = input()
while not command == "Done":
    token = command.split(" ")
    if token[1] == "Right":
        right(int(token[2]))
    elif token[1] == "Left":
        left(int(token[2]))
    elif token[1] == "Odd":
        odd()
    elif token[1] == "Even":
        even()
    command = input()

print(f"You crafted {''.join(weapon_name)}!")