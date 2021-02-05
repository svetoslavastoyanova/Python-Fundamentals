allowed_quantity = int(input())
days_left = int(input())


christmas_spirit = 0
budget = 0
for days in range(1, days_left + 1):
    if days % 11 == 0:
        allowed_quantity += 2
    if days % 2 == 0:
        budget += allowed_quantity*2
        christmas_spirit += 5
    if days % 3 == 0:
        budget += allowed_quantity*5
        budget += allowed_quantity*3
        christmas_spirit += 13
    if days % 5 == 0:
        budget += allowed_quantity * 15
        christmas_spirit += 17
        if days % 3 == 0:
            christmas_spirit += 30
    if days % 10 == 0:
        christmas_spirit -= 20
        budget += 23
        if days == days_left:
            christmas_spirit -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {christmas_spirit}")
