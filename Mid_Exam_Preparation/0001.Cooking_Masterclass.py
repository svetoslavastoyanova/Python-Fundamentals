import math
budget = float(input())
students = int(input())
price_of_flour = float(input())
price_for_one_egg = float(input())
price_of_one_apron = float(input())
free_packages = students/5

formula = price_of_one_apron*math.ceil(students*1.2) + price_for_one_egg*10*(students) + price_of_flour*(students - free_packages)

if formula <= budget:
    print(f"Items purchased for {math.ceil(formula):.2f}$.")
else:
    print(f"{(formula - budget):.2f}$ more needed.")

