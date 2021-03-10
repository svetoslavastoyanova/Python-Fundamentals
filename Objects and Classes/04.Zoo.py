class Zoo:
    __animals = 0
    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammals":
            self.mammals.append(name)
        elif species == "fishes":
            self.fishes.append(name)
        elif species == "birds":
            self.birs.append(name)

    def get_info(self, species):
        result = ""
        if species == "mammals":
            result += f"Mammals in {self.name}: ", "{names}"