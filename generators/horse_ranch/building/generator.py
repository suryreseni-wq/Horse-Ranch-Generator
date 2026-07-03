@register_generator(priority=20)
class BuildingGenerator(GeneratorModule):

    name = "Buildings"

    def generate(self, engine):

        print("Generating buildings...")
