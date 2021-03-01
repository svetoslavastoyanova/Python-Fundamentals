numbers = list(map(lambda x: int(x), input().split(', ')))
beggars = int(input())
beggars_list = [0]*beggars
for i in range(len(numbers)):
    element = numbers[i]
    beggars_index = i % len(beggars_list)
    beggars_list[beggars_index] += element
print(beggars_list)

