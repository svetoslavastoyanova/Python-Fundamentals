interval = int(input())
capacity = 255
sum = 0

for liters in range(1, interval + 1):
    quantities = int(input())
    if (sum + quantities) > capacity:
        print(f"Insufficient capacity!")
    else:
        sum += quantities
print(sum)