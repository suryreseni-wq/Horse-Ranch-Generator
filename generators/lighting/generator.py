@register_generator(priority=90)
class LightingGenerator(GeneratorModule):

    name = "Lighting"

    def generate(self, engine):

        print("Generating lighting...")
