from dataclasses import dataclass

@dataclass
class LightingSettings:

    use_sun: bool = True

    sun_energy: float = 4.0

    sun_angle: float = 0.5

    use_world_light: bool = True

    hdri: str | None = None

    exposure: float = 0.0
