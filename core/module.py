from abc import ABC, abstractmethod


class GeneratorModule(ABC):

    name = "Module"

    @abstractmethod
    def generate(self, engine):
        pass

    def cleanup(self, engine):
        pass
