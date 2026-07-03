import bpy
import bmesh

from math import radians
from mathutils import Matrix


class MeshBuilder:

    def __init__(self, name):

        self.mesh = bpy.data.meshes.new(name)
        self.object = bpy.data.objects.new(name, self.mesh)

        bpy.context.collection.objects.link(self.object)

        self.bm = bmesh.new()

        self.last_geom = []

        self.current_material = None

    def box(self, width, length, height):

        result = bmesh.ops.create_cube(
            self.bm,
            size=1
        )

        verts = result["verts"]

        scale = Matrix.Diagonal((
            width / 2,
            length / 2,
            height / 2,
            1
        ))

        bmesh.ops.transform(
            self.bm,
            matrix=scale,
            verts=verts
        )

        self.last_geom = verts

        return self

    def plane(self, width, length):

        result = bmesh.ops.create_grid(
            self.bm,
            x_segments=1,
            y_segments=1,
            size=1
        )

        verts = result["verts"]

        scale = Matrix.Diagonal((
            width / 2,
            length / 2,
            1,
            1
        ))

        bmesh.ops.transform(
            self.bm,
            matrix=scale,
            verts=verts
        )

        self.last_geom = verts

        return self

    def translate(self, x, y, z):

        bmesh.ops.translate(
            self.bm,
            verts=self.bm.verts,
            vec=(x, y, z)
        )

        return self

    def rotate(self, x=0, y=0, z=0):

        matrix = (
            Matrix.Rotation(radians(x), 4, 'X') @
            Matrix.Rotation(radians(y), 4, 'Y') @
            Matrix.Rotation(radians(z), 4, 'Z')
        )

        bmesh.ops.transform(
            self.bm,
            matrix=matrix,
            verts=self.bm.verts
        )

        return self

    def scale(self, x, y, z):

        matrix = Matrix.Diagonal((
            x,
            y,
            z,
            1
        ))

        bmesh.ops.transform(
            self.bm,
            matrix=matrix,
            verts=self.bm.verts
        )

        return self

    def finish(self):

        self.bm.normal_update()

        self.bm.to_mesh(self.mesh)

        self.mesh.update()

        self.bm.free()

        return self.object
