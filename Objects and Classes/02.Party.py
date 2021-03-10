class Party:
    def __init__(self):
        self.people = []

    def going_people(self):
        return ", ".join([p for p in self.people])

party = Party()
line = input()
while line != "End":
    party.people.append(line)
    line = input()


print(f"Going: {party.going_people()}")
print(f"Total: {len(party.people)}")
