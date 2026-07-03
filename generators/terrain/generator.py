from core.module import GeneratorModule
from core.registry import register_generator
from core.mesh_builder import MeshBuilder

@register_generator(priority=0)
class TerrainGenerator(GeneratorModule):

    name = "Terrain"

    def generate(self, engine):

        terrain = MeshBuilder("Terrain")

        terrain.plane(
            width=engine.config.terrain_size,
            length=engine.config.terrain_size
        )

        terrain.subdivide(120)

        terrain.material("grass")

        terrain.finish()
