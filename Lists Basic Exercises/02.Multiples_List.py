factor = int(input())
count = int(input())
list = []

for number in range(1, count + 1):
    if number*factor != 0:
        result = number*factor
        list.append(result)
print(list)
