import bpy


class ForgeProperties(bpy.types.PropertyGroup):

    site_diameter: bpy.props.FloatProperty(
        name="Diameter",
        default=200.0,
        min=10
    )

    tree_count: bpy.props.IntProperty(
        name="Trees",
        default=80,
        min=0
    )

    horse_count: bpy.props.IntProperty(
        name="Horses",
        default=8,
        min=0
    )


def register():

    bpy.utils.register_class(ForgeProperties)

    bpy.types.Scene.forge = bpy.props.PointerProperty(
        type=ForgeProperties
    )


def unregister():

    del bpy.types.Scene.forge

    bpy.utils.unregister_class(ForgeProperties)
