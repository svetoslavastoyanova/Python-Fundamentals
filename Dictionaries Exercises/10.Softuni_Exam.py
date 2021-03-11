line = input()
results = {}
submissions = {}
while line != "exam finished":
    tokens = line.split("-")
    name = tokens[0]
    language = tokens[1]

    if language == "banned":
        if name in results:
            del results[name]

    elif language != "banned":
        points = int(tokens[2])
        if name not in results:
            results[name] = []
        results[name].append(points)

        if language not in submissions:
            submissions[language] = 0
        submissions[language] += 1

    line = input()

print("Results:")
for key, value in sorted(results.items(), key=lambda x: x[1], reverse=True):
    value = max(value)
    print(f"{key} | {value}")
print("Submissions:")
for key, value in sorted(submissions.items(), key=lambda x: x[0]):
    print(f"{key} - {value}")






