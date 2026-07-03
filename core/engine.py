from core.registry import get_generators
from core.logger import Logger
from core.entity_manager import EntityManager
from core.scene import SceneManager
from core.materials import MaterialLibrary
from core.randomizer import Randomizer


class RanchEngine:

    def __init__(self, config):

        self.config = config

        self.logger = Logger()

        self.scene = SceneManager()

        self.materials = MaterialLibrary()

        self.entities = EntityManager()

        self.random = Randomizer(config.random_seed)

        self.modules = []

    def discover_generators(self):

        self.modules.clear()

        for generator_class in get_generators():

            generator = generator_class()

            self.modules.append(generator)

            self.logger.info(
                f"Loaded generator: {generator.name}"
            )

    def initialize(self):

        self.logger.info("Initializing Engine")

        self.scene.set_metric()

    def generate(self):

        self.initialize()

        self.discover_generators()

        self.logger.info(
            f"{len(self.modules)} generators loaded."
        )

        for generator in self.modules:

            self.logger.info(
                f"Running {generator.name}"
            )

            generator.generate(self)

        self.logger.finish()
