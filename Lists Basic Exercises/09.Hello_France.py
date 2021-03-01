types = input().split("|")
budget = float(input())
new_price = []
last_price = 0
for item in types:
    items = item.split("->")
    type = items[0]
    price = float(items[1])

    if type == "Clothes" and price > 50 or type == "Shoes" and price > 35 or type == "Accessories" and price > 20.50:
        continue
    if price > budget:
        continue
    else:
        budget -= price
        current_profit = price*0.4
        last_price += current_profit
        new_price.append(price + current_profit)

for x in new_price:
    print(f"{x:.2f}", end=" ")

print()
print(f"Profit: {last_price:.2f}")

budget += sum(new_price)
if budget >= 150:
    print(f"Hello, France!")
else:
    print(f"Time to go.")





