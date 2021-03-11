line = input()
dict_price = {}
dict_quantity = {}

while line != "buy":
    tokens = line.split()
    product = tokens[0]
    price = float(tokens[1])
    quantity = float(tokens[2])

    if product not in dict_price and product not in dict_quantity:
        dict_price[product] = price
        dict_quantity[product] = quantity
    else:
        dict_quantity[product] += quantity
        dict_price[product] = price

    line = input()

for key, value in dict_price.items():
    total_price = value * dict_quantity[key]
    print(f"{key} -> {total_price:.2f}")