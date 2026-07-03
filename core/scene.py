import bpy


class SceneManager:

    def __init__(self):

        self.scene = bpy.context.scene

    def clear(self):

        bpy.ops.object.select_all(action="SELECT")
        bpy.ops.object.delete(use_global=False)

    def set_metric(self):

        self.scene.unit_settings.system = "METRIC"
        self.scene.unit_settings.scale_length = 1.0

    def collection(self, name):

        if name in bpy.data.collections:
            return bpy.data.collections[name]

        col = bpy.data.collections.new(name)

        self.scene.collection.children.link(col)

        return col
