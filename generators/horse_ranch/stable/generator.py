class StableBuilder:

    def __init__(self, engine):

        self.engine = engine

        self.width = 18

        self.length = 40

        self.height = 8

        self.location = (0,0,0)

        self.floors = 2

    def size(self,w,l,h):

        self.width = w

        self.length = l

        self.height = h

        return self

    def floors(self,n):

        self.floors = n

        return self

    def location(self,x,y,z):

        self.location=(x,y,z)

        return self

    def build(self):

        mesh = MeshBuilder("Stable")

        mesh.box(
            self.width,
            self.length,
            self.height
        )

        return mesh.finish()
