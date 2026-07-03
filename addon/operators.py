import bpy

from core.engine import RanchEngine
from core.config import RanchConfig


class FORGE_OT_generate(
    bpy.types.Operator
):

    bl_idname = "forge.generate"

    bl_label = "Generate"

    bl_description = "Generate procedural scene"

    def execute(self, context):

        props = context.scene.forge

        config = RanchConfig()

        config.site_diameter = props.site_diameter
        config.tree_count = props.tree_count
        config.horse_count = props.horse_count

        engine = RanchEngine(config)

        engine.generate()

        self.report(
            {'INFO'},
            "Generation finished."
        )

        return {'FINISHED'}


def register():

    bpy.utils.register_class(
        FORGE_OT_generate
    )


def unregister():

    bpy.utils.unregister_class(
        FORGE_OT_generate
    )
