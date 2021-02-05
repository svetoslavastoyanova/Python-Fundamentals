budget = float(input())
price_per_kilo = float(input())
one_pack_eggs_price = 0.75 * price_per_kilo
one_litre_milk_price = price_per_kilo + (0.25 * price_per_kilo)
needed_milk_price = 0.250 * one_litre_milk_price
one_cozonac_price = price_per_kilo + needed_milk_price + one_pack_eggs_price
money = 0
count_cozonac = 0
coloured_eggs = 0
while budget > one_cozonac_price:
    budget -= one_cozonac_price
    count_cozonac += 1
    coloured_eggs += 3
    if count_cozonac % 3 == 0:
        coloured_eggs -= count_cozonac - 2
print(f"You made {count_cozonac} cozonacs! Now you have {coloured_eggs} eggs and {budget:.2f}BGN left.")


