from dataclasses import dataclass

@dataclass
class VegetationSettings:

    tree_count: int = 80

    bush_count: int = 40

    grass_density: float = 0.7

    random_seed: int = 1337
