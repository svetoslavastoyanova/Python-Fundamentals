line = input().split("\\")

for words in line:
    if "." in words:
        tokens = words.split(".")
        file_name = tokens[0]
        file_extension = tokens[1]
        print(f"File name: {file_name}")
        print(f"File extension: {file_extension}")
