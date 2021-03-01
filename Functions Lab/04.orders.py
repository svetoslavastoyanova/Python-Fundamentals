def calculate(name, quantity):
    price = None
    if name == "coffee":
        price = 1.5
    if name == "water":
        price = 1.0
    if name == "coke":
        price = 1.4
    if name == "snacks":
        price = 2.0
    if price is not None:
        return price*quantity


product = input()
quantity = int(input())
print(f'{calculate(product, quantity):.2f}')