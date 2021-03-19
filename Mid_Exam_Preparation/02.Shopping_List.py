list = input().split("!")
command = input()

while command != "Go Shopping!":
    tokens = command.split(" ")
    command_type = tokens[0]
    item = tokens[1]

    if command_type == "Urgent":
        if not item in list:
            list.insert(0, item)

    elif command_type == "Unnecessary":
        if item in list:
            list.remove(item)

    elif command_type == "Correct":
        if item in list:
            new_item = tokens[2]
            current_index = list.index(item)
            list[current_index] = new_item

    elif command_type == "Rearrange":
        if item in list:
            list.remove(item)
            list.append(item)

    command = input()

result = ", ".join(list)
print(f"{result}")