import re
regex = r"([@|#|$|^])"
line = input().split(", ")

for t in line:
    ticket = t.strip()
    if not len(ticket) == 20:
        print("invalid ticket")
        continue
    if len(ticket) == 20:
        match = re.findall(regex, ticket)
        if match == []:
            print(f'ticket "{ticket}" - no match')
            continue
        symbol = match[0]
        left_side = ticket[0:10]
        right_side = ticket[10:20]
        if symbol * 10 == left_side and symbol*10 == right_side:
            print(f'ticket "{ticket}" - 10{symbol} Jackpot!')
        elif symbol*6 in right_side and symbol*6 in left_side:
            count_left = left_side.count(symbol)
            count_right = right_side.count(symbol)
            count = min(count_left, count_right)
            print(f'ticket "{ticket}" - {count}{symbol}')
        else:
            print(f'ticket "{ticket}" - no match')






