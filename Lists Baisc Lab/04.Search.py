n = int(input())
word = input()
string = []
filtered_strings = []
for _ in range(n):
    strings = input()
    string.append(strings)
    if word in strings:
        filtered_strings.append(strings)
print(string)
print(filtered_strings)

