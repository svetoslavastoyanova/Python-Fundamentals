usernames = input().split(", ")
valid_username = []
symbol_one = "-"
symbol_two = "_"
is_valid = False
for username in usernames:
    if 3 <= len(username) < 16:
        is_valid = True
        if username.isalnum() or symbol_one in username or symbol_two in username:
            valid_username.append(username)

print("\n".join(valid_username))
