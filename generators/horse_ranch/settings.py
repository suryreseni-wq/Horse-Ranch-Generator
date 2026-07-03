from dataclasses import dataclass

@dataclass
class HorseRanchSettings:

    stable_count: int = 22

    stable_floors: int = 2

    arena_width: float = 70

    arena_length: float = 45

    horse_count: int = 10

    fence_height: float = 1.6
