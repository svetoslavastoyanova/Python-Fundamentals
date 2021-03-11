line = input()
sides = {}
while line != "Lumpawaroo":
    if " | "in line:
        tokens = line.split(" | ")
        forceside = tokens[0]
        forceuser = tokens[1]
        if forceside not in sides:
            sides[forceside] = []
        if forceuser not in sides:
            sides[forceside].append(forceuser)

    elif " -> " in line:
        tokens = line.split(" -> ")
        forceuser = tokens[0]
        forceside = tokens[1]
        if forceuser in sides:
            for key, value in sides.items():
                sides[key].remove(forceuser)
                sides[forceside].append(forceuser)
                print(f"{forceuser} joins the {forceside} side!")
                continue
        elif forceuser not in sides:
            sides[forceside].append(forceuser)
            print(f"{forceuser} joins the {forceside} side!")









    line = input()