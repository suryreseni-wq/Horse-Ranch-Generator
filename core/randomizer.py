import random


class Randomizer:

    def __init__(self, seed):

        self.random = random.Random(seed)

    def float(self, a, b):

        return self.random.uniform(a, b)

    def int(self, a, b):

        return self.random.randint(a, b)

    def choice(self, items):

        return self.random.choice(items)

    def bool(self):

        return self.random.random() > 0.5
