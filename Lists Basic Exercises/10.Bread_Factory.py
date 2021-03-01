line = input().split("|")
coins = 100
energy = 100
completed = True

for command in line:
    current = command.split("-")
    if current[0] == "rest":
        added_energy = int(current[1])
        if energy + added_energy <= 100:
            energy += added_energy
            print(f"You gained {added_energy} energy.")
        else:
            print(f"You gained {0} energy.")
        print(f"Current energy: {energy}.")

    elif current[0] == "order":
        new_coins = int(current[1])
        if energy - 30 >= 0:
            coins += new_coins
            energy -= 30
            print(f"You earned {new_coins} coins.")
        else:
            energy += 50
            print(f"You had to rest!")
    else:
        ingredient = current[0]
        cost = int(current[1])

        if coins <= 0:
            completed = False
            print(f"Closed! Cannot afford {ingredient}.")
            break

        if coins - cost > 0:
            coins -= cost
            print(f"You bought {ingredient}.")
        else:
            completed = False
            print(f"Closed! Cannot afford {ingredient}.")
            break
if completed:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")

