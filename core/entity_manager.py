class EntityManager:

    def __init__(self):

        self.entities = []

    def add(self, entity):

        self.entities.append(entity)

    def remove(self, entity):

        self.entities.remove(entity)

    def clear(self):

        self.entities.clear()

    def find(self, name):

        for e in self.entities:

            if e.name == name:

                return e

        return None
