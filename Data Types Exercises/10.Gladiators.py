lost_fight_counts = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_expenses = 0.0
sword_expenses = 0.0
shield_expenses = 0.0
armor_expenses = 0.0
year_expenses = 0.0
for game in range(1, lost_fight_counts + 1):
    if game % 2 == 0:
        helmet_expenses += 1
    if game % 3 == 0:
        sword_expenses += 1
    if game % 2 == 0 and game % 3 == 0:
        shield_expenses += 1
        if shield_expenses % 2 == 0:
            armor_expenses += 1
    year_expenses = helmet_expenses*helmet_price + sword_expenses*sword_price + shield_expenses*shield_price + armor_expenses*armor_price
print(f"Gladiator expenses: {year_expenses:.2f} aureus")