from dataclasses import dataclass

@dataclass
class RoadSettings:

    width: float = 6.0

    radius: float = 100.0

    resolution: int = 128

    material: str = "gravel"
