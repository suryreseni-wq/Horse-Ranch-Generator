import bpy


class MaterialLibrary:

    def __init__(self):

        self.cache = {}

    def create(self, name, color):

        if name in self.cache:
            return self.cache[name]

        mat = bpy.data.materials.new(name)

        mat.use_nodes = True

        bsdf = mat.node_tree.nodes["Principled BSDF"]

        bsdf.inputs["Base Color"].default_value = (
            color[0],
            color[1],
            color[2],
            1
        )

        self.cache[name] = mat

        return mat
