import random

class Platform:
    def __init__(self, level, resources):
        self.level = level
        self.resources = resources

    def distribute_resources(self, amount):
        if amount > self.resources:
            print(f"Ei piisa ressursse tasemelt {self.level} (alles {self.resources} ressursse).")
            return 0
        else:
            self.resources -= amount
            return amount


class Resource:
    def __init__(self, name, initial_amount):
        self.name = name
        self.amount = initial_amount 
        self.initial_amount = initial_amount 

    def reduce(self, amount):
        if amount > self.amount:
            print(f"Ei piisa {self.name} ressursse ({self.amount} alles).")
            return 0
        else:
            self.amount -= amount 
            return amount


class Game:
    def __init__(self, num_levels, initial_resources):
        self.num_levels = num_levels
        self.initial_resources = initial_resources
        self.platforms = [Platform(level, initial_resources) for level in range(1, num_levels + 1)]
        self.resource = Resource("Ressurss", initial_resources) 

    def run(self):
        remaining_resources = self.resource.amount 
        total_taken = 0  

        for platform in self.platforms:
            print(f"Platvorm {platform.level}, ressursse: {remaining_resources}")

            random_amount = random.randint(0, remaining_resources) 
            amount_taken = platform.distribute_resources(random_amount)
            total_taken += amount_taken 
            remaining_resources -= amount_taken

            print(f"Platvorm {platform.level} lõpptulemus, ressursse: {amount_taken}")
            print(f"Järgmisele platvormile jääb {remaining_resources} ressursse.\n")


game = Game(num_levels=10, initial_resources=100)
game.run()
