line = input()
dictionary = {}
while line != "End":
    tokens = line.split(" -> ")
    company = tokens[0]
    number = tokens[1]
    if company not in dictionary:
        dictionary[company] = []
    if number not in dictionary[company]:
        dictionary[company].append(number)

    line = input()


for key, value in sorted(dictionary.items(), key=lambda x: x[0]):

    print(key)
    for id in value:
        print(f"-- {id}")