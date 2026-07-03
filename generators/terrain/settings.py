from dataclasses import dataclass

@dataclass
class TerrainSettings:

    size: float = 260.0

    subdivisions: int = 120

    noise_strength: float = 0.35

    noise_scale: float = 24.0

    material: str = "grass"
