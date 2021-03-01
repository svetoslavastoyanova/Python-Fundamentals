def perform(a, b, operation):
    if operation == "add":
        return a + b
    if operation == "subtract":
        return a - b
    if operation == "divide":
        return int(a / b)
    if operation == "multiply":
        return a * b


operation = input()
a = int(input())
b = int(input())
print(perform(a, b, operation))
