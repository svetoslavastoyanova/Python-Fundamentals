#Вариант 1 (по-добрият вариант, тъй като при промяна на стойностите трябва винаги да ги промнеянме навсякъде, а
#с мин и макс не е необходимо.
MIN_NUMBER = 1
MAX_NUMBER = 100
while True:
    n = float(input())
    if MIN_NUMBER <= n <= MAX_NUMBER:
        print(f"The number {n} is between {MIN_NUMBER} and {MAX_NUMBER}")
        break

#Вариант 2
while True:
    n = float(input())
    if 1 <= n <= 100:
        print(f"The number {n} is between 1 and 100")
        break