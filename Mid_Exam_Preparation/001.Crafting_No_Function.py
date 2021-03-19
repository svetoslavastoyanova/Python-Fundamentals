particles = input().split("|")
line = input()
list = []
while line != "Done":
    tokens = line.split(" ")

    if tokens[1] == "Right":
        index = int(tokens[2])
        if 0 <= index+1 < len(particles) and 0 <= index < len(particles):
            particles[index], particles[index+1] = particles[index+1], particles[index]

    elif tokens[1] == "Left":
        index = int(tokens[2])
        if 0 <= index-1 < len(particles) and 0 <= index < len(particles):
            particles[index], particles[index-1] = particles[index-1], particles[index]

    elif tokens[1] == "Odd":
        for i in range(len(particles)):
            if i%2 != 0:
                list.append(particles[i])
        print(" ".join(list))

    elif tokens[1] == "Even":
        for i in range(len(particles)):
            if i%2 == 0:
                list.append(particles[i])
        print(" ".join(list))

    line = input()
result = "".join(particles)
print(f"You crafted {result}!")
