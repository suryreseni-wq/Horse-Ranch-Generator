scene = Ranch()

scene.terrain()

scene.circular_road(
    radius=100
)

scene.add_stables(
    count=22
)

scene.add_arena()

scene.add_trees(
    density=0.65
)

scene.add_horses(10)

scene.build()
