import bpy


class FORGE_PT_panel(
    bpy.types.Panel
):

    bl_label = "Forge Engine"

    bl_idname = "FORGE_PT_panel"

    bl_space_type = "VIEW_3D"

    bl_region_type = "UI"

    bl_category = "Forge"

    def draw(self, context):

        layout = self.layout

        props = context.scene.forge

        layout.prop(
            props,
            "site_diameter"
        )

        layout.prop(
            props,
            "tree_count"
        )

        layout.prop(
            props,
            "horse_count"
        )

        layout.separator()

        layout.operator(
            "forge.generate",
            icon='OUTLINER_OB_MESH'
        )


def register():

    bpy.utils.register_class(
        FORGE_PT_panel
    )


def unregister():

    bpy.utils.unregister_class(
        FORGE_PT_panel
    )
