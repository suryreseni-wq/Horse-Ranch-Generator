bl_info = {
    "name": "Forge Engine",
    "author": "suryreseni-wq",
    "version": (0, 1, 0),
    "blender": (4, 2, 0),
    "location": "View3D > Sidebar > Forge",
    "description": "Procedural generation engine for Blender",
    "category": "Object",
}

from . import ui
from . import operators
from . import properties


def register():

    properties.register()

    operators.register()

    ui.register()


def unregister():

    ui.unregister()

    operators.unregister()

    properties.unregister()
