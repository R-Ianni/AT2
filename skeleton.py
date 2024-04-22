class Skeleton(Enemy):
    def __init__(self, level):
        super().__init__("Skeleton", level, health=30 * level, damage=7 * level)

    # Add additional methods or attributes specific to skeletons if needed