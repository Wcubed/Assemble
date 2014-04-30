__author__ = 'wybe'


class Building:
    """
    Base building class.

    Instanced when a building is built.
    """

    size = (1, 1)
    # Size in tiles of the building

    effect_radius = 0
    # The amount of tiles this building can effect in a square around the building
    # '0' means only the tiles the building is on are effected

    item_name = "i_"
    # Name of the item to drop when destroyed, starts with "i_"

    def __init__(self, x, y):

        self.x = x
        self.y = y


class Item:
    """
    Base item class.

    Instanced when items lay on the ground.
    Queried when information about an item is needed
    """

    is_buildable = False
    # Specifies if an item can be built

    building_name = "b_"
    # Name of the building to be built, starts with "b_"

    def __init__(self, x, y):

        self.x = x
        self.y = y