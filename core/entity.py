from dataclasses import dataclass
from mathutils import Vector


@dataclass
class Entity:

    name: str

    location: Vector

    rotation: Vector

    scale: Vector

    blender_object = None
