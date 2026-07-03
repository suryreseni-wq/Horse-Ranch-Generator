from dataclasses import dataclass

@dataclass
class RanchConfig:

    site_diameter: float = 200.0

    tree_count: int = 80

    horse_count: int = 8

    floors: int = 2

    road_width: float = 5.0

    random_seed: int = 1337

    terrain_size: float = 260.0
