from core.module import GeneratorModule
from core.registry import register_generator
from core.builder import RoadBuilder


@register_generator(priority=10)
class RoadGenerator(GeneratorModule):

    name = "Roads"

    def generate(self, engine):

        (
            RoadBuilder(engine)
            .circle(
                radius=100,
                width=6
            )
            .material("gravel")
            .build()
        )
