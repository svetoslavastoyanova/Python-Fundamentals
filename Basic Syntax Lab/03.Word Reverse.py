#Вариант 1
word = input()
reversed_word = ""

for c in reversed(word):
    reversed_word += c
print(reversed_word)

#Вариант 2
word = input()
reversed_word = ""

for index in range(len(word) - 1, -1, -1):
    reversed_word += word[index]
print(reversed_word)